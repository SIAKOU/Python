from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from DjangoProjectexposer.models import Client, Adresse
from django.shortcuts import render, redirect, get_object_or_404
from DjangoProjectexposer.usercreationform import UserCreateForm


# Create your views here.
def form(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        img = request.FILES.get('img', None)
        email = request.POST['email']

        new_Client = Client(nom=nom, prenom=prenom, img_client=img, email=email)
        new_Client.save()

        img_dir = new_Client.img_client
        return redirect('ajouter_adresse', id_client=new_Client.id_client)
    return render(request, 'form.html')


def Adresse_Choice(request, id_client):
    client = get_object_or_404(Client, id_client=id_client)
    img = client.img_client
    if request.method == 'POST':
        num_rue = request.POST['num_rue']
        nom_rue = request.POST['nom_rue']
        city = request.POST['city']
        state = request.POST['state']
        longitude = request.POST['longitude']
        latitude = request.POST['latitude']

        new_Adresse = Adresse(num_rue=num_rue, nom_rue=nom_rue, city=city, state=state, longitude=longitude,
                              latitude=latitude, id_client_id=id_client)
        new_Adresse.save()
        clients_details = Client.objects.get(id_client=id_client)
        adresse = new_Adresse
        return render(request, 'Client_details.html', {'details': clients_details, 'adresse': adresse})
    return render(request, 'Adresse_Choice.html', {'img': img})


def map(request):
    return render(request, 'map.html')


def client(request):
    clients = Client.objects.all()

    # Ajouter les adresses à chaque client
    for client in clients:
        client.adresses = Adresse.objects.filter(id_client=client)

    return render(request, 'Client_list.html', {'per': clients})


def client_details(request, id_client):
    clients_details = get_object_or_404(Client, id_client=id_client)
    # Vous n'avez pas besoin d'ajouter manuellement les adresses
    return render(request, 'Client_details.html', {'details': clients_details})


def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreateForm()
    return render(request, 'create_users.html', {'form': form})


def Home(request):
    return render(request, 'Home.html')
