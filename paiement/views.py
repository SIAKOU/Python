import uuid

from django.shortcuts import render
from django.utils import timezone

from DjangoProjectexposer.models import Client, Marchandise, Paiement


def paiements_invalides(request):
    invalid_paiements = Paiement.objects.select_related('client').filter(est_valide=False)
    return render(request, 'paiement/li_paiements_invalides.html', {'invalid_paiements': invalid_paiements})


def liste_paiements(request):
    paiements = Paiement.objects.select_related('client').all()
    return render(request, 'paiement/li_payements.html', {'paiements': paiements})


def enregister_paiement(request):
    if request.method == 'POST':
        try:
            client_id = request.POST['client']
            client = Client.objects.get(id=client_id)  # Corrected: Fetch client by ID
            marchandises_data = request.POST.getlist('marchandise')
            montant_total = request.POST['montant_total']

            # Process selected merchandise items
            marchandises = []
            for marchandise_id in marchandises_data:
                marchandise = Marchandise.objects.get(numero_marchandise=marchandise_id)  # Fetch marchandise object
                marchandises.append(marchandise)  # Append the marchandise object

            paiement = Paiement(
                est_valide=True,
                client=client,
                montant_total=montant_total,
                date_paiement=timezone.now(),
                token=uuid.uuid4()
            )
            paiement.save()
            for marchandise in marchandises:  # Add marchandises using ManyToMany relationship
                paiement.marchandises.add(marchandise)

            return render(request, 'paiement/enregistrer_paiement.html', {
                'clients': Client.objects.all(),
                'marchandises': Marchandise.objects.all(),
                'success_message': "Le paiement a été enregistré avec succès !"  # Success message
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
