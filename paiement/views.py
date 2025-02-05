import uuid
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
import xml.etree.ElementTree as ET
import json

from DjangoProjectexposer.models import Client, Marchandise, Paiement


def paiements_invalides(request):
    invalid_paiements = Paiement.objects.filter(est_valide=False).order_by('-date_paiement')
    return render(request, 'paiement/li_paiements_invalides.html', {'invalid_paiements': invalid_paiements})



def search_marchandises(request):
    query = request.GET.get('q', '')
    results = Marchandise.objects.filter(nom__icontains=query).values('numero_marchandise', 'nom', 'prix')[:10]
    return JsonResponse(list(results), safe=False)


def liste_paiements(request):
    paiements = Paiement.objects.select_related('client').all().order_by('-date_paiement')
    return render(request, 'paiement/li_payements.html', {'paiements': paiements})


def enregister_paiement(request):
    if request.method == 'POST':
        try:
            client_id = request.POST['client']
            client = Client.objects.get(id_client=client_id)  # Corrected: Fetch client by ID
            marchandises_data = request.POST.getlist('marchandise')
            montant_total = request.POST['montant_total']

            # Process selected merchandise items and prepare JSON data
            marchandises = []
            for marchandise_id in marchandises_data:
                marchandise = Marchandise.objects.get(numero_marchandise=marchandise_id)  # Fetch marchandise object
                marchandises.append({
                    'numero_marchandise': marchandise.numero_marchandise,
                    'nom': marchandise.nom,
                    'description': marchandise.description,
                    'prix': marchandise.prix
                })

            paiement = Paiement(
                est_valide=True,
                client=client,
                marchandises=marchandises,  # Save as JSON
                montant_total=montant_total,
                date_paiement=timezone.now(),
                token=uuid.uuid4()
            )
            paiement.save()

            return render(request, 'paiement/enregistrer_paiement.html', {
                'clients': Client.objects.all(),
                'marchandises': Marchandise.objects.all(),
                'success_message': "Le paiement a été enregistré avec succès !",  # Success message
                'show_banner': True  # Show banner for 5 seconds
            })

        except Exception as e:
            print(f"Error during payment processing: {e}")
            return render(request, 'paiement/enregistrer_paiement.html', {  # Render error on same page
                'clients': Client.objects.all(),
                'marchandises': Marchandise.objects.all(),
                'error_message': f"Une erreur est survenue : {e}"  # Display specific error message
            })

    clients = Client.objects.all()
    marchandises = Marchandise.objects.all()
    return render(request, 'paiement/enregistrer_paiement.html', {'clients': clients, 'marchandises': marchandises})


def supprimer_paiement(request, id_paiement):
    paiement = get_object_or_404(Paiement, numero_paiement=id_paiement)
    if request.method == 'POST':
        # Vérifie si le bouton "supprimer" a été activé
        if "supprimer" in request.POST:
            paiement.delete()
            return redirect('listePaiements')
            # Affiche une page de confirmation pour la suppression
    return render(request, 'paiement/supprimer_paiement.html', {'details': paiement})


#creation de la vue qui permet de telecharger le recu de paiement
def telecharger_recu(request, id_paiement):
    paiement = get_object_or_404(Paiement, numero_paiement=id_paiement)

    if request.method == 'POST':
        format = request.POST.get('format')  # reception du format de fichier a telecharger   

        if format == 'xml':
            # Creation de la structure du fichier xml
            root = ET.Element("recu")
            ET.SubElement(root, "numero_paiement").text = str(paiement.numero_paiement)
            ET.SubElement(root, "client").text = paiement.client.nom
            ET.SubElement(root, "montant_total").text = str(paiement.montant_total)
            ET.SubElement(root, "date_paiement").text = paiement.date_paiement.strftime('%Y-%m-%d %H:%M:%S')

            marchandises = paiement.marchandises  # Directly use the JSON field
            marchandises_element = ET.SubElement(root, "marchandises")  # Definition des element de la marchandise dans le fichier xml
            for marchandise in marchandises:
                marchandise_element = ET.SubElement(marchandises_element, "marchandise")
                ET.SubElement(marchandise_element, "numero_marchandise").text = str(marchandise['numero_marchandise'])
                ET.SubElement(marchandise_element, "nom").text = marchandise['nom']
                ET.SubElement(marchandise_element, "description").text = marchandise['description']
                ET.SubElement(marchandise_element, "prix").text = str(marchandise['prix'])

            # je suis sur que vous avez compris 😊😊
            recu_xml = ET.tostring(root, encoding='utf-8', method='xml')

            #Creation du fichier  http response avec le contenu xml
            response = HttpResponse(recu_xml, content_type='application/xml')
            response['Content-Disposition'] = f'attachment; filename="recu_{paiement.numero_paiement}.xml"'

        elif format == 'txt':
            # Craetion de la sttucture du recu en TXT 
            recu_txt = f"Reçu de Paiement\n"
            recu_txt += f"Numéro de Paiement: {paiement.numero_paiement}\n"
            recu_txt += f"Client: {paiement.client.nom}\n"
            recu_txt += f"Montant Total: {paiement.montant_total}\n"
            recu_txt += f"Date de Paiement: {paiement.date_paiement.strftime('%Y-%m-%d %H:%M:%S')}\n"
            recu_txt += f"Marchandises:\n"

            for marchandise in paiement.marchandises:
                recu_txt += f"  - Numéro: {marchandise['numero_marchandise']}\n"
                recu_txt += f"    Nom: {marchandise['nom']}\n"
                recu_txt += f"    Description: {marchandise['description']}\n"
                recu_txt += f"    Prix: {marchandise['prix']} £ \n"
                
            # 
            response = HttpResponse(recu_txt, content_type='text/plain')
            response['Content-Disposition'] = f'attachment; filename="recu_{paiement.numero_paiement}.txt"'

        else:
            return HttpResponse("Format non supporté", status=400)

        return response

    return render(request, 'paiement/telecharger_recu.html', {'paiement': paiement})

