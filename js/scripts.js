$(document).ready(function(){
    $(window).scroll(function() {
        var scroll = $(window).scrollTop();
        if(scroll>50){
            $("#navbar").css("background",#10caca);
        }else{
            $("#navbar").css("background",#ffffff);
        }
    })
  })