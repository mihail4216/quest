/**
 * Created by mihail on 27.02.17.
 */



    $.ajax({
        type:'GET',
        url:'more/',
        data:{
            user_name: $('#us').val()

        },
        dataType:'html'
    });














// $('.get-more').click(function(){
//         alert(1233333);
//         $.ajax({
//             type: "GET",
//             url: "news/more/",
//             success: function(data) {
//                 for(i = 0; i < data.length; i++){
//                     $('ul').append('<li>'+data[i]+'</li>');
//                 }
//             }
//         });
//
//     });
// alert(133);
// $(document).ready(function() {
//
//     // AJAX GET
//     alert(123);
//     $('.get-more').click(function(){
//         alert(1233333);
//         $.ajax({
//             type: "GET",
//             url: "news/more/",
//             success: function(data) {
//             for(i = 0; i < data.length; i++){
//                 $('ul').append('<li>'+data[i]+'</li>');
//             }
//         }
//         });
//
//     });
//     });
//
//
//
//
//
//

//                              SCRF CODE

// function getCookie(name) {
//         var cookieValue = null;
//         var i = 0;
//         if (document.cookie && document.cookie !== '') {
//             var cookies = document.cookie.split(';');
//             for (i; i < cookies.length; i++) {
//                 var cookie = jQuery.trim(cookies[i]);
//                 // Does this cookie string begin with the name we want?
//                 if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                     break;
//                 }
//             }
//         }
//         return cookieValue;
//     }
//     var csrftoken = getCookie('csrftoken');
//
//     function csrfSafeMethod(method) {
//         // these HTTP methods do not require CSRF protection
//         return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
//     }
//     $.ajaxSetup({
//         crossDomain: false, // obviates need for sameOrigin test
//         beforeSend: function(xhr, settings) {
//             if (!csrfSafeMethod(settings.type)) {
//                 xhr.setRequestHeader("X-CSRFToken", csrftoken);
//             }
//         }
//     });