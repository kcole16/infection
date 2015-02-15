$(document).ready(function() {
    $('.results').hide();
    $('.fake_results').hide();
    $('.btn-danger').click( function() {
        var user = $(this).attr('id');
        $.ajax({
            url: '/start_infection/',
            type: 'get',
            data: {user:user},
            success: function(response){
                $('.infected').text(response['total_infected'])
                $('.fake_results').hide();
                location.reload();
            }
        });
    });
    $('.btn-success').click( function() {
        var user = $(this).attr('id');
        console.log(user);
        $.ajax({
            url: '/estimate_infection/',
            type: 'get',
            data: {user:user},
            success: function(response){
                $('.fake_infected').text(response['infected'])
                $('.results').hide();
                $('.fake_results').show();
            }
          });
     });
});






