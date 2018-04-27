var finishGrandPyWrite = false;
var numberLineText = 0;
$(function () {
    $.fn.scrollBottom = function () {
        return $(this).scrollTop($(this)[0].scrollHeight);
    };
    var $question_papy;
    $question_papy = $('#questionpapy');
    $question_papy.on('submit', function (e) {
        e.preventDefault();
        var response;
        var text = $('#question').val();
        if (finishGrandPyWrite === true) {
            $("#chatBox").append("Me : " + text + "</br>").scrollBottom();
            finishGrandPyWrite = false;
            $.ajax({
                url: 'question',
                type: 'POST',
                data: JSON.stringify({'grandfather_question': text}),
                datatype: 'json',
                contentType: "application/json; charset=utf-8",
                success: function (data) {

                    if (data.correct_question === true) {
                        response = {
                            correct_question: true,
                            googlemaps_result: data.googlemaps_result,
                            wikipedia_result: data.wikipedia_result
                        };
                    }
                    if (data.correct_question === false) {

                        response = {
                            correct_question: false
                        };

                    }
                }

            });
            $("#chatBox").append("<span id='tempory" + numberLineText + "'>" + "GrandPYBot : En train de réfléchir " + "<img src='../static/assets/img/Eclipse-1s-200px.svg' height='30' width='30'>" + "</span>").scrollBottom().delay(3000).queue(function () {
                $('#tempory' + numberLineText).last().remove();
                if (response.correct_question === true) {
                    $("#chatBox").append("<span id='response" + numberLineText + "'>" + "</span>" + "</br>").scrollBottom();
                    typed = new Typed('#response' + numberLineText, {
                        strings: ["GrandPYBot : " + randomResponse],
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
                            $('#googlemaps').show('slow');
                            $('#responseQuestion').show('slow');
                            $('#responseQuestion').text(response.wikipedia_result);
                            map.setZoom(16);
                            map.setCenter({lat: response.googlemaps_result.lat, lng: response.googlemaps_result.lng});
                            $("#chatBox").clearQueue().finish();
                            numberLineText += 1;
                        },
                        loop: false
                    });
                }
                if (response.correct_question === false) {
                    $("#chatBox").append("<span id='response" + numberLineText + "'>" + "</span>" + "</br>").scrollBottom();
                    typed = new Typed('#response' + numberLineText, {
                        strings: ["GrandPYBot : Je n'ai pas compris la question, peux tu répéter"],
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

                            $("#chatBox").clearQueue().finish();
                            numberLineText += 1;
                        },
                        loop: false
                    });
                }
            });


        }
    });
    console.log("ready ask question");

});


