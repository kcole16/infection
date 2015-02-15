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
  });
