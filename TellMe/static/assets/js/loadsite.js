var randomResponse;
var randomError;
var keystrokeSound = new Audio('https://vocaroo.com/media_command.php?media=s1mhvLTNIFaW&command=download_mp3');

function playSound() {
    keystrokeSound.pause();
    keystrokeSound.currentTime = 1;
    keystrokeSound.play();
    firstOpenSite = false
}

$(window).on('load', function () {
    


   
    $.ajax({
        url: 'loadsite',
        type: 'POST',
        data: JSON.stringify({'loadsite': 'start'}),
        datatype: 'json',
        contentType: "application/json; charset=utf-8",
        success: function (data) {
            randomResponse = data.randomResponse;
            randomError = data.randomError;
            typed = new Typed('#chatBox', {
                strings: ['GrandPyBot : Bienvenue cher utilisateur', 'GrandPyBot : ' + data.randomHello + '</br>'],
                typeSpeed: 40,
                backSpeed: 30,
                backDelay: 900,
                startDelay: 1000,
                smartBackspace: true,
                showCursor: false,
                preStringTyped: function (array, self) {
                    playSound();
                },
                onComplete: function (array, self) {
                    finishGrandPyWrite = true;
                },
                loop: false

            });
        }
    });
    console.log("ready loadsite");
});