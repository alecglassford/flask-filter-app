var map = L.map('map').setView([47.55, -122.2], 10);
var mapquestLayer = new L.TileLayer('http://{s}.mqcdn.com/tiles/1.0.0/map/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: 'Data, imagery and map information provided by <a href="http://open.mapquest.co.uk" target="_blank">MapQuest</a>,<a href="http://www.openstreetmap.org/" target="_blank">OpenStreetMap</a> and contributors.',
    subdomains: ['otile1','otile2','otile3','otile4']
});
map.addLayer(mapquestLayer);
if (data) {
    var dataLayer = L.geoJson(data, {
        pointToLayer: function (feature, latlng) {
            if (feature.properties.status == 'Unsatisfactory'){
                return L.circleMarker(latlng, {color: 'red', fillOpacity: '0.8', radius: 5});
            }
            return L.circleMarker(latlng, {color: 'green', fillOpacity: '0.6', radius: 5});
        },
        onEachFeature: function(feature, layer) {
            layer.bindPopup(
                '<a href="' + encodeURIComponent(feature.properties.id) + '/">' +
                    feature.properties.full_name +
                '</a>'
            );
        }
    });
    map.addLayer(dataLayer);
}
else if (latlong) {
    map.setView(latlong, 15);
    var marker = L.marker(latlong).addTo(map);
}
