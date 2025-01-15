// Initialisation de la carte
var map = L.map('map').setView([51.505, -0.09], 13);

// Ajout des tuiles OpenStreetMap
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// Fonction pour convertir l'adresse en coordonnées
async function geocodeAddress(address) {
    const apiKey = 'YOUR_API_KEY'; // Remplacez par votre clé API OpenCage
    const apiUrl = `https://api.opencagedata.com/geocode/v1/json?q=${encodeURIComponent(address)}&key=${apiKey}&pretty=1`;

    try {
        const response = await fetch(apiUrl);
        const data = await response.json();

        if (data.results && data.results.length > 0) {
            const { lat, lng } = data.results[0].geometry;
            return { lat, lng };
        } else {
            alert("Aucune coordonnée trouvée pour cette adresse.");
            return null;
        }
    } catch (error) {
        console.error("Erreur lors du géocodage : ", error);
        alert("Une erreur s'est produite lors de la recherche de l'adresse.");
        return null;
    }
}

// Fonction pour afficher un popup avec les informations
function displayPopup(lat, lng, info) {
    const marker = L.marker([lat, lng]).addTo(map);
    const popupContent = `
        <b>${info.nom}</b><br>
        ${info.prenom}<br>
        Adresse : ${info.address}<br>
        Latitude : ${lat}<br>
        Longitude : ${lng}
    `;
    marker.bindPopup(popupContent).openPopup();
    map.setView([lat, lng], 13); // Centrer la carte sur le marqueur
}

// Récupération des champs d'entrée
const form = document.querySelector('form');
form.addEventListener('submit', async function (e) {
    e.preventDefault();

    const nom = document.querySelector('input[name="nom"]').value;
    const prenom = document.querySelector('input[name="prenom"]').value;
    const numRue = document.querySelector('input[name="num_rue"]').value;
    const nomRue = document.querySelector('input[name="nom_rue"]').value;
    const city = document.querySelector('input[name="city"]').value;
    const state = document.querySelector('input[name="state"]').value;

    // Construire l'adresse complète
    const address = `${numRue} ${nomRue}, ${city}, ${state}`;
    document.getElementById('full_address').value = address;

    // Convertir l'adresse en coordonnées
    const coordinates = await geocodeAddress(address);
    if (coordinates) {
        // Afficher un popup avec les informations
        displayPopup(coordinates.lat, coordinates.lng, { nom, prenom, address });
    }
});
