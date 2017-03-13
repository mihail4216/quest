/**
 * Created by mihail on 04.03.17.
 */
$(document).ready(function () {
    var photo_s = true;
    $('#photo').click(function () {
        // $(this).css('center','center');
        if (photo_s) {
            $(this).animate({

                width: $(this).width() * 3,
                height: $(this).height() * 3
            });
            photo_s = false;
        }
        else {
            $(this).animate({
                width: $(this).width() /3,
                height: $(this).height() / 3
            });
            photo_s = true;
        }
    })


});