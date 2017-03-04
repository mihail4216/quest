/**
 * Created by mihail on 01.03.17.
 */
$(document).ready(function () {
    // $('#news_one').attr()
    var show_num=5;
    var news1 = $('.news_more');
    for(i=0;i<show_num;i++){
            $(news1[i]).show();
        }

$('#show').click(function () {
    var news = $('.news_more');
    for(i=5; i<show_num+5;i++){

        $(news[i]).show(500);

    }
    show_num+=5;
    if(show_num>news.length){
        $('#show').hide();
    }

});




$("#find_bt").click(function () {
$.ajax({
            type: 'GET',
            url: "/news/find/",
            data: {
                news_name: $('#find_word').val()

            },
            cache:false,
            success : function (response) {
                    console.log(response);
                    $('#false_news').hide();
                    $('#true_news').show();
                    $('#news_all').hide();
                    $('#find_news_block').html('<div><h2><a href="/news/' + response['id'] + '">' + response['title'] + '</a></h2><h3>' + response['text'] + '</h3><h5><a id="like">Лайки: ' + response['likes'] + '</a></h5><h5>Автор:<a href="/accounts/' + response['avtor_id'] + '/"> ' + response['avtor'] + '</a></h5></div>')

            },
            error: function () {
                    $('#true_news').hide();
                    $('#false_news').show();
                    $('#find_news_block').html('');
                    $('#news_all').show();

            }

        });

});
 // <div id="news_one" class="news_more" style="display: none">
//  <h2><a href="/news/{{ newsone.id }}/">{{ newsone.title }}</a></h2>
 // <h3>{{ newsone.text }}</h3>
 // <h5><a id="like">Лайки: {{ newsone.likes }}</a></h5>
 // <h5>Автор:<a href="/accounts/{{ newsone.avtor.id }}/"> {{ newsone.avtor.username }}</a></h5>
 // <br>



});