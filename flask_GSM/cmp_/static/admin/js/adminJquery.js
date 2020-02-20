
$(document).ready(function(){
  $('#add_device').keyup(function() {
    search_query = $('#add_device').val();
    ul = $("#device_search_option");
    ul.empty();

    if(search_query.length>0)
    {

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
                    $('#selected_device').append('<div id="'+id+'" class="alert alert-success selected_device"   role="alert">'+name+' <span class="selection_close" style="float:right" aria-hidden="true">&times;</span> </div>')
                });
                $('#add_device_slider').click(function(){

                    var selected_device_id = [];
                    $('#selected_device').find('div').each(function(){selected_device_id.push(this.id)})
                    $.ajax({
                        type:'GET',
                        url:'/addDevicesToslider',
                        data:{'key':JSON.stringify(selected_device_id)},
                        success:function(data)
                        {
                            if(data=='True')
                            {
                                location.reload();

                            }
                        },
                        error:function(data)
                        {
                            alert(data)
                        }
                    });


                });
            }
        });
    }
  });

  $('.btn btn-outline-danger delete_button').click(function(){
    //   let id = $this.attr('data-device-id');
      alert('id');
  });

//   $('.closeButton').click(function(){
//     $('#add_new_model_content').empty();
//     $('#add_device').val('');
//   });
    
});
