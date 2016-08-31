$(document).ready(function() {
    $('form').submit(function(event) {
        event.preventDefault();
        $.ajax({
            url: {% url 'posts' %},
            method: "post",
            data: $(this).serialize(),
            success: function(serverResponse) {
                $('.posts').html(serverResponse);
            }
        });
    });
});
