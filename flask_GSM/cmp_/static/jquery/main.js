  $(document).ready(function() {
      var count = $('.abc div');
      var searchUrl = $('#inpUrls').data('searchUrl');
      var compareUrl = $('#inpUrls').data('compareUrl');
      var seachNavUrl = $('#inpUrls').data('searchNavUrl');
      for (i = 8; i < count.length; i++) {
          $(".col-md-3:nth-child(" + i + ")").hide();
      }
      $('#show').click(function() {
          for (i = 8; i < count.length; i++) {
              $(".col-md-3:nth-child(" + i + ")").toggle();
          }
      });

      $('#search_phone').keyup(function() {
          search_query = $('#search_phone').val();
          ul = $('#append');
          ul.empty();
          if (search_query.length > 0) {
              // alert(search_query.length);
              search_val = $('#search_phone').val();
              // alert(search_val);
              $.ajax({
                  type: "GET",
                  url: searchUrl,
                  data: { "value": search_val },
                  // dataType:"json",
                  success: function(data) {
                      data = JSON.parse(data);
                      console.log(typeof(data));
                      for (i = 0; i < data.length; i++) {
                          ul.append(`<li><a href="/phone_details/${data[i].brand}/${data[i].slug}/${data[i].slug}"> ${data[i].name} </a> </li>`);
                          // console.log(data.length);
                      }
                  },
                  error: function(data) {
                      alert('error');
                  }
              });
          }
      });

      $('#cmp_first').keyup(function() {
          search_query = $('#cmp_first').val();
          ul = $('#cmp_first_dd');
          ul.empty();
          if (search_query.length > 0) { // alert(search_query.length);
              search_val = $('#cmp_first').val();
              // alert(search_val);
              $.ajax({
                  type: "GET",
                  url: searchUrl,
                  data: { 'value': search_val },
                  // dataType:"json",
                  success: function(data) {
                      data = JSON.parse(data);
                      for (i = 0; i < data.length; i++) {
                          ul.append('<li><a href="" class="click_1" id="' + data[i].id + '">' + data[i].name + '</a> </li>');
                      }
                      $('.click_1').click(function(e) {
                          e.preventDefault();
                          var first_id = $(this).attr('id');
                          var first_name = $(this).text();
                          console.log(first_name);
                          $('#selected_1').html('<div class="alert alert-warning alert-dismissible fade show" role="alert">' + first_name + '<p  class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></p></div>');
                          $('#selected_1').attr('find', first_id);
                          ul.empty();
                      });
                  },
                  error: function(data) {
                      alert('error');
                  }
              });
          }
      });

      $('#cmp_second').keyup(function() {
          // alert('anuj');
          search_query = $('#cmp_second').val();
          ul = $('#cmp_second_dd');
          ul.empty();
          if (search_query.length > 0) {
              search_val = $('#cmp_second').val();
              // alert(search_val);
              $.ajax({
                  type: "GET",
                  url: searchUrl,
                  data: { 'value': search_val },
                  // dataType:"json",
                  success: function(data) {
                      data = JSON.parse(data);
                      for (i = 0; i < data.length; i++) {
                          ul.append('<li><a href="" class="click_2" id="' + data[i].id + '">' + data[i].name + '</a> </li>');
                      }
                      $('.click_2').click(function(e) {
                          e.preventDefault();
                          var second_id = $(this).attr('id');
                          var second_name = $(this).text();
                          console.log(second_name);
                          $('#selected_2').html('<div class="alert alert-warning alert-dismissible fade show" role="alert">' + second_name + '<p  class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></p></div>');
                          $('#selected_2').attr('find', second_id);
                          ul.empty();
                      });
                  },
                  error: function(data) {
                      alert('error');
                  }
              });
          }
      });
      $('#phone_compare_button').click(function() {
          var first_phone_id = $('#selected_1').attr('find');
          var second_phone_id = $('#selected_2').attr('find');
          let url = `${compareUrl}?phone1=${first_phone_id}&phone2=${second_phone_id}`;
          window.location.href = url;
      });


      $('#add_device_slider').click(function() {
          var selected_device = $('#selected_1').attr('find');
          // var second_phone_id = $('#selected_2').attr('find');
          alert(selected_device)
      });

      $("#search_phone_outer").autocomplete({
          source: function(request, response) {
              let search_val = $('#search_phone_outer').val();
              $.ajax({
                  url: seachNavUrl,
                  data: { "value": search_val },
                  success: function(data) {
                      response(data);
                  }
              });
          },
          minLength: 2,
          select: function(event, ui) {
              url = `/${ui.item.brand}/${ ui.item.slug}/${ ui.item.id}`;
              location.href = url;
          }
      });
  });