// if grand py write
var finishGrandPyWrite = false;
var numberLineText = 1;
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
        // if "grand py bot" no longer writes
        if (finishGrandPyWrite === true) {
            var chatbox = $("#chatBox");
            chatbox.append("<img src='../static/assets/img/avatar.png' height='30' width='30'>" + "<span id='question" + numberLineText + "'>" + "</span>").scrollBottom();

            $('#question' + numberLineText).append("Moi : " + text + "</br>");
            finishGrandPyWrite = false;
            // Send the question by ajax to the server
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
            chatbox.append("<span id='tempory" + numberLineText + "'>" + "<img src='../static/assets/img/dimitri.png' height='30' width='30'>" + "GrandPYBot : En train de réfléchir " + "<img src='../static/assets/img/Eclipse-1s-200px.svg' height='30' width='30'>" + "</span>").scrollBottom().delay(3000).queue(function () {
                $('#tempory' + numberLineText).last().remove();
                if (response.correct_question === true) {
                    chatbox.append("<img src='../static/assets/img/dimitri.png' height='30' width='30'>" + "<span  id='responseGoogleMaps" + numberLineText + "'>" + "</span>").scrollBottom();
                    typed = new Typed('#responseGoogleMaps' + numberLineText, {
                        strings: ["GrandPYBot : " + "Voici le lieu que j'ai trouvé" + "</br>"],
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
                            chatbox.scrollBottom();
                            var responseQuestion = $('#responseQuestion');
                            $('#googlemaps').show('slow');
                            map.setZoom(16);
                            map.setCenter({lat: response.googlemaps_result.lat, lng: response.googlemaps_result.lng});
                            chatbox.append("<img src='../static/assets/img/dimitri.png' height='30' width='30'>" + "<span  id='responseWikipedia" + numberLineText + "'>" + "</span>").scrollBottom()
                            typed = new Typed('#responseWikipedia' + numberLineText, {
                                strings: ["GrandPYBot : " + randomResponse + "</br>"],
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
                                    chatbox.scrollBottom();
                                    finishGrandPyWrite = true;
                                    var responseQuestion = $('#responseQuestion');
                                    $('#googlemaps').show('slow');
                                    responseQuestion.empty();
                                    responseQuestion.show('slow');
                                    responseQuestion.text(response.wikipedia_result);
                                    chatbox.clearQueue().finish();
                                    numberLineText += 1;
                                },
                                loop: false
                            });
                        },
                        loop: false
                    });

                }
                if (response.correct_question === false) {
                    chatbox.append("<img src='../static/assets/img/dimitri.png' height='30' width='30'>" + "<span id='response" + numberLineText + "'>" + "</span>" + "</br>").scrollBottom();
                    typed = new Typed('#response' + numberLineText, {
                        strings: ["GrandPYBot : " + randomError],
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

                            chatbox.clearQueue().finish();
                            numberLineText += 1;
                        },
                        loop: false
                    });
                }
            });


        }
    });
    console.log("Ready ask question");

});


