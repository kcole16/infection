  $(document).ready(function() {
    $('.make_users').click( function() {
        $.ajax({
            url: '/create_fake_users/',
            type: 'get',
            success: function(response){
                console.log(response);
                location.reload();
                // $('.infected').text(response['total_infected'])
            }
          });
     });
    $('.btn').click( function() {
        $.ajax({
            url: '/limited_infection/',
            type: 'post',
            data: $('form').serialize(),
            dataType: 'json',
            success: function(response){
                console.log(response);
                location.reload();
                // $('.infected').text(response['total_infected'])
            }
          });
     });
    $('.total_infection').click( function() {
        $.ajax({
            url: '/total_infection/',
            type: 'get',
            success: function(response){
              console.log(response);
              location.reload();
            }
          });
     });
    $('.disinfect').click( function() {
        $.ajax({
            url: '/disinfect/',
            type: 'get',
            success: function(response){
              console.log(response);
              location.reload();
            }
          });
     });
    $('.clear').click( function() {
        $.ajax({
            url: '/clear_users/',
            type: 'get',
            success: function(response){
              console.log(response);
              location.reload();
            }
          });
     });
  });
