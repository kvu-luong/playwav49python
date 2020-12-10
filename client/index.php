<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>GUI PLAY audio</title>
        <link rel="stylesheet" href="css/style.css">
        <link rel="author" href="humans.txt">
    </head>
    <body>
        Test play audio
        <button id="js-play">Play audio</button>
        <button id="js-stop">Stop</button>
        <button id="js-pause">Pause</button>
       <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/3.0.4/socket.io.js" integrity="sha512-aMGMvNYu8Ue4G+fHa359jcPb1u+ytAF+P2SCb+PxrjCdO3n3ZTxJ30zuH39rimUggmTwmh2u7wvQsDTHESnmfQ==" crossorigin="anonymous"></script>
		<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
		<script>
		  const socket = io('http://localhost:8080');
          $('#js-play').on('click', function(){
             socket.emit('play', 'heelelel');
          })
          $('#js-stop').on('click', function(){
             socket.emit('stop', 'heelelel');
          })
           $('#js-pause').on('click', function(){
             socket.emit('pause', 'heelelel');
          })
		</script>
    </body>
</html>
