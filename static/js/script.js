
$(function() {
    var server='localhost';
    var port="5000"
    var uri="chat"
    function appendRequest(request){
      $('#chatWindow').append('<p class="text-primary">'+request+'<p>');
    }
    function appendResponse(response){
         $('#chatWindow').append('<p class="text-success">'+response+'<p>');
    }


  /*  $( "#userInput" ).focus(function() {
            $('#heading').css('visibility', 'hidden');
        });

        $( "#userInput" ).focusout(function() {
            $('#heading').css('visibility', 'visible');
        }); 
*/
            $( "#chatForm" ).submit(function( event ) {
                event.preventDefault();
                if(!$('#userInput').val())
                    return;
                var request=$('#userInput').val();
                appendRequest(request);
                $.ajax({
                    type: 'POST',
                    url: 'http://localhost:5000/chat',//server+"/"+post+"/"+uri,
                    data: JSON.stringify ({message: request}),
                    success: function(data) { appendResponse(data); },
                    error: function(data){console.log("Something went wrong");},
                    contentType: "application/json",
                });

                $('#userInput').val("");
                window.scrollTo(0,document.body.scrollHeight);

            });
    
        });