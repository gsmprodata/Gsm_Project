
$(document).ready(function(){
  $('#add_device').keyup(function() {
    search_query = $('#add_device').val();
    ul = $('#device_search_option');
    ul.empty();

    if(search_query.length>0)
    {
        $("#device_search_option").html("");

        $.ajax({
            type:"GET",
            url:'/search_phone',
            data: { "value": search_query },
            success:function(output)
            {
                suggestion_array = JSON.parse(output);
                console.log(suggestion_array);
                for (i=0;i<suggestion_array.length;i++){
                $('#device_search_option').append('<div  ><a href="#" data-click='+suggestion_array[i]['id']+' class="row suggestedDevice">'+suggestion_array[i]['name']+'</a></div>');
                }
                $('.suggestedDevice').click(function(){
                    id = $(this).attr('data-click');
                    name = $(this).html();
                    $('#selected_device').append('<div id="'+id+'" class="alert alert-success"   role="alert">'+name+' </div>')
                });
            }
        });
    }
  });

  $('.closeButton').click(function(){
      alert('asdasd');
  });
    
});
