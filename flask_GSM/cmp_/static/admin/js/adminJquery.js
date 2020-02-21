
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

$('#tableSlider').on('click','.delete_button',function(){
    id = $(this).data('device-id');
    $('#device_to_delete').data('delete-id',id);
    delete_id = $('#device_to_delete').data('delete-id');
    $('#delete_device_from_slider').on('click',function(){
        $.ajax({
             type:'GET',
             url:'/deleteDeviceFromSlider',
             data :{'id':delete_id},
             success:function(data)
             {
                if(data=='True')
                {
                    $( "#tableSlider").load(window.location.href + " #tableSlider");
    
                }
             },
             error:function(data)
            {
                alert(data);
            }
        })
    })
});


});
