document.addEventListener("DOMContentLoaded", function() {
    const map = L.map('map').setView([0, 0], 2);  // Center the map
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

    let marker;

    map.on('click', function (e) {
        if (marker) {
            map.removeLayer(marker);
        }

        marker = L.marker([e.latlng.lat, e.latlng.lng]).addTo(map);
        
        document.getElementById("id_point").value = `POINT(${e.latlng.lng} ${e.latlng.lat})`;  // WKT format for PointField
        document.getElementById("id_latitude").value = e.latlng.lat;
        document.getElementById("id_longitude").value = e.latlng.lng;
    });
});
