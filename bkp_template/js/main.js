$(function() {
    $(window).scroll(function(){
        var window_scrolltop = $(window).scrollTop();
        var div1 = $('.retro_logo').position().top;
        var speed =  2;
        if(window_scrolltop < $('.retro_logo').height()){
          $('.retro_logo').css('background-position', '50% ' + ((div1 + window_scrolltop) / speed ) + 'px');
      };
  })     
})