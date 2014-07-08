/**
 * Created by franklin on 6/24/14.
 */
$(function(){
    $('#search').keyup(function(){
        $.ajax({
            type:"POST",
            url:"/article/search",
            data:{
                'search_text':$('#search').val(),
                'csrfmiddlewaretoken': $("input[name= csrfmiddlewaretoken]").val()
            },
            success:searchSuccess,
            dataType:'html'
        });
    });

    $('#like').click(function(){
        var article_id;
        article_id = $(this).attr("data-id");
        $.get('/article/like/',{"article_id":article_id},function(data){
            $('#like_count').html(data);
            $('#like').prop('disabled',true);
        });
    });

    $('#bookmark').click(function(){
        var article_id;
        article_id = $(this).attr("data-id");
        $.get('/article/bookmark/',{"article_id":article_id},function(data){
            $('#bookmark').prop('disabled',true);
        });
    });

    $('.delete_p').click(function(){
       var procedure_id;
       procedure_id=$(this).attr("data-id");
        $.get('/article/delete_procedure/',{"procedure_id":procedure_id},function(data){
            $('#procedure'+procedure_id).empty();
        });
    });
});

function searchSuccess(data,textStatus,jqXHR)
{
    $('#search_results').html(data);
}