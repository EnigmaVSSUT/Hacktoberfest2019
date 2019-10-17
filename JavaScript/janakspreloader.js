<script type="text/javascript">

var images = new Array();

function preloadImages(){

    for (i=0; i < preloadImages.arguments.length; i++){

         images[i] = new Image();

        images[i].src = preloadImages.arguments[i];

    }

}

preloadImages("logo.jpg", "main_bg.jpg", "body_bg.jpg", "header_bg.jpg");

</script>
