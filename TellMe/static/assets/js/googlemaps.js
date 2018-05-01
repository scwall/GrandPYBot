var map;
$(document).ready(function () {


    function initialize() {
        map = new google.maps.Map(document.getElementById('googlemaps'));


    }

    google.maps.event.addDomListener(window, 'load', initialize);
    $.fn.scrollBottom = function () {
        return $(this).scrollTop($(this)[0].scrollHeight);
    };
});

