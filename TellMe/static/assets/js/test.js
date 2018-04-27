$(document).ready(function () {

    jQuery('#tester').click(function () {
        $('#maper').show('slow');
        $('#texter').show('slow');
        $("#chatBox").append("\nSomething here\n\nAgain").scrollBottom();

        console.log('test');
        map.setZoom(16);
        map.setCenter({lat: 50, lng: 5});

    });
});
// je suis beau