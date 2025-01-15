// Initialisation de la carte
var map = L.map('map').setView([51.505, -0.09], 13);
var nom = document.getElementById('nom').value;
var prenom = document.getElementById('prenom').value;
var latitude = document.getElementById('latitude').value;
var longitude = document.getElementById('longitude').value;

// Ajout des tuiles OpenStreetMap
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// Ajout d'un marqueur
var marker = L.marker([51.505, -0.09]).addTo(map);

// Contenu du popup
var popupContent = `
    <b>${nom}</b><br>
    ${prenom}<br>
    Latitude : ${latitude}<br>
    Longitude : ${longitude}
`;
marker.bindPopup(popupContent).openPopup();
///////////////////////////////////////////////////////

// Gérer les clics pour déplacer le marqueur et ajouter une popup
map.on('click', function (e) {
    var lat = e.latlng.lat;
    var lng = e.latlng.lng;

    // Mise à jour du marqueur
    marker.setLatLng([lat, lng]);

    // Exemple de récupération des valeurs des champs d'entrée

    var popupContent = `Nom: ${nom}<br>Prénom: ${prenom}<br>Latitude: ${lat}<br>Longitude: ${lng}`;
    marker.bindPopup(popupContent).openPopup();

    // Centrer la carte sur le marqueur
    map.setView([lat, lng], 13);
});
