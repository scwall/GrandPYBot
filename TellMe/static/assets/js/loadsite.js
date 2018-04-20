$(window).on('load', function () {
    $.ajax({
        url: 'loadsite',
        type: 'POST',
        data: JSON.stringify({'loadsite': 'start'}),
        datatype: 'json',
        contentType: "application/json; charset=utf-8",
        success: function (data) {
            $('#loadSiteHello').text(data.randomResponse);
        }
    });
    console.log("ready loadsite");
});