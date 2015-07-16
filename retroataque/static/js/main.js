$(function() {
	/*Minimal paralax effect*/
    $(window).scroll(function(){
        var window_scrolltop = $(window).scrollTop();
        var div1 = $('.retro_logo').position().top;
        var speed =  2;
        if(window_scrolltop < $('.retro_logo').height()){
          $('.retro_logo').css('background-position', '50% ' + ((div1 + window_scrolltop) / speed ) + 'px');
      };
  	});
  	/*Init lightbox*/
  	$(".bg_body_lecture").find("img").click(function(){
  		$("#lighbox_all").attr("href", $(this).attr("src"));
  		$("#lighbox_all").attr("data-title", $(this).attr("alt"));
  		$("#lighbox_all").click()
  	});
    /*Force external link in new tab*/
    $("a[href^='http']").attr('target','_blank');

})
