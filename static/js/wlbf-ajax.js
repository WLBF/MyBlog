$(document).ready(function() {

       $('#suggestion').keyup(function(){
          var query;
          query = $(this).val();
          $.get('/wlbf/suggest_category/', {suggestion: query}, function(data){
          $('#cats').html(data);
        });
     });


});
