  $(document).ready(function(){
    var count = $('.abc div');
    for(i=8;i<count.length;i++)
    {
      $( ".col-md-3:nth-child("+i+")" ).hide();

    }
    $('#show').click(function(){
      for(i=8;i<count.length;i++)
      {
        $( ".col-md-3:nth-child("+i+")" ).toggle();
      }

    });

    $('#search_phone').keyup(function(){
      search_query = $('#search_phone').val();
      ul=$('#append');
      ul.empty();
      if(search_query.length>0)
      {
        // alert(search_query.length);
        search_val = $('#search_phone').val();
        // alert(search_val);
        $.ajax({
          type:"GET",
          url:"{% url 'search_phone' %}",
          data:{'value':search_val},
          // dataType:"json",
          success:function(data){
            console.log(data);

            for(i=0;i<data.length;i++)
            {

              ul.append('<li><a href="/blog/pro/'+data[i].id+'">'+data[i].name+'</a> </li>');
            }

          },
          error:function(data){
            alert('error');
          }

        });
      }
    });

    $('#cmp_first').keyup(function(){
      search_query = $('#cmp_first').val();
      ul=$('#cmp_first_dd');
      ul.empty();
      if(search_query.length>0)
      {
        // alert(search_query.length);
        search_val = $('#cmp_first').val();
        // alert(search_val);
        $.ajax({
          type:"GET",
          url:"{% url 'search_phone' %}",
          data:{'value':search_val},
          // dataType:"json",
          success:function(data){
            // console.log(data);

            for(i=0;i<data.length;i++)
            {

              ul.append('<li><a href="" class="click_1" id="'+data[i].id+'">'+data[i].name+'</a> </li>');

            }
            $('.click_1').click(function(e){
              e.preventDefault();
              var first_id = $(this).attr('id');
              var first_name = $(this).text();
              console.log(first_name);
              $('#selected_1').html('<div class="alert alert-warning alert-dismissible fade show" role="alert">'+first_name+'<p  class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></p></div>');
              $('#selected_1').attr('find',first_id);
              ul.empty();

            });

          },
          error:function(data){
            alert('error');
          }

        });
      }
    });

    $('#cmp_second').keyup(function(){
      // alert('anuj');
      search_query = $('#cmp_second').val();
      ul=$('#cmp_second_dd');
      ul.empty();


    });





  });
