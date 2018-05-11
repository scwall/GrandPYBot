//initialize googlemaps
var myLatLng;
var map;
var marker;
$(document).ready(function () {


    function initialize() {
        map = new google.maps.Map(document.getElementById('googlemaps'));
        marker = new google.maps.Marker();
        marker.setMap(map);
    }


    google.maps.event.addDomListener(window, 'load', initialize);

});

