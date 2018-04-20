$(function () {
    var $question_papy;
    $question_papy = $('#questionpapy');
    $question_papy.on('submit', function (e) {
        e.preventDefault();
        var text = $('#question').val();
        $.ajax({
            url: 'question',
            type: 'POST',
            data: JSON.stringify({'grandfather_question': text}),
            datatype: 'json',
            contentType: "application/json; charset=utf-8",
            success: function (data) {
                console.log(data);
                alert(data.wikipedia_result);
            }
        });

    });
    console.log("ready ask question");
});


