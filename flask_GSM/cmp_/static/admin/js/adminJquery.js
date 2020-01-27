
$(document).ready(function(){
  $('#add_device').keyup(function() {
    search_query = $('#add_device').val();
    ul = $('#append');
    ul.empty();
    if (search_query.length > 0) {
        // alert(search_query.length);
        search_val = $('#add_device').val();
        // alert(search_val);
        $.ajax({
            type: "GET",
            url: '/search_phone',
            data: { "value": search_val },
            // dataType:"json",
            success: function(data) {
                data = JSON.parse(data);
                console.log(typeof(data));
                for (i = 0; i < data.length; i++) {
                    ul.append(`<li><a href="/phone_details/${data[i].name}/${data[i].id}"> ${data[i].name} </a> </li>`);
                    // console.log(data.length);
                }
            },
            error: function(data) {
                alert('error');
            }
        });
      }
  });
});
