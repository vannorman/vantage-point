$(document).ready(function(){
	$('input').on('click',function(){
		$(this).focus();
		$(this).select();
	});
	min=18;
	max=99;
	carouselWidth = $('.carousel_container').width();
	for(i=min;i<max;i++){
		if (i == 31) {
			SelectAge(31);
			$('.carousel').append("<li class='selected'>"+i+"</li>");
			
		} else {
			$('.carousel').append("<li>"+i+"</li>");

		}
	}
	ageWidth = $('.carousel li').width();
	$('.carousel').width((max-min)*ageWidth);
	$('.carousel li').on('click',function(){
		$('.selected').each(function(){ $(this).removeClass('selected'); });	
		$(this).addClass('selected');
		SelectAge($(this).text());
	});
	
});

var ageWidth = 40;
var carouselWidth = 40;
function SelectAge(age){
	ml = (-(age - min) * ageWidth) + carouselWidth/2 + "px"
	$('.carousel').animate({marginLeft: ml});
	
}
