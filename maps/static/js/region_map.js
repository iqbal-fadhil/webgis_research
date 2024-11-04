document.addEventListener("DOMContentLoaded", function() {
    const map = L.map('map').setView([0, 0], 2);  // Center the map
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

    let drawnPolygon;

    map.on('click', function (e) {
        if (drawnPolygon) {
            map.removeLayer(drawnPolygon);
        }
        
        const latlngs = [[e.latlng.lat, e.latlng.lng]];  // Example to start a polygon
        drawnPolygon = L.polygon(latlngs, {color: 'blue'}).addTo(map);

        document.getElementById("id_polygon").value = JSON.stringify(latlngs);  // Update the polygon field with coordinates
    });
});
