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




	// Gender
	$('.gender ul li').click(function(){
		$('.gender ul li').each(function(){
			$(this).removeClass('selected');
		});
		$(this).addClass('selected');
	});

	$('.sexual-orientation ul li').click(function(){
		$('.sexual-orientation ul li').each(function(){
			$(this).removeClass('selected');
		});
		$(this).addClass('selected');
	});

	// Any scale select
	$('#pre-assessment .display_trigger .options ul li').click(function(){
		var els =$(this).closest('.item').attr('display_trigger_elements').split(',') ;
		for (el in els){
			var div = "#"+els[el];
			var tex =$(this).text().trim();
			var arr = ["YES","Kind of"];
			var t = $.inArray($(this).text(),["YES","Kind of"]) ;
			var flag = $.inArray(tex,arr);
			console.log('flag:'+flag+", inarr("+tex+","+arr);
			if (flag > -1){
				
				$(div).show();	
			} else {
				$(div).hide();	
			}
	

		}
	});
//	$('#pre-assessment .item .options ul li.square').click(function(){
		$('.square').on('click',function(){ 
			Clicked($(this),'.square');
			return;
		});
		$('.dynamic').on('click',function(){ 
			Clicked($(this),'.dynamic');
			return;
		});
//			var els =$(this).closest('.item').attr('display_trigger_elements').split(',') ;
//			$(this).closest('ul').find('.square').each(function(){ 
//				console.log('removing from:'+$(this).attr('class'));
//				$(this).removeClass('selected').removeClass('green').removeClass('red');
//			});	
//			$(this).addClass('selected');
//			if (parseInt($(this).text()) in [1,2,'x']){
//				$(this).addClass('red');
//			} else {
//				$(this).addClass('green');
//
//			}
//		});

});

function Clicked($this, el){
	var els =$this.closest('.item').attr('display_trigger_elements').split(',') ;
	$this.closest('ul').find(el).each(function(){ 
		$(this).removeClass('selected').removeClass('green').removeClass('red');
	});	
	$this.addClass('selected');
	if (parseInt($this.text()) in [1,2,'x']){
		$this.addClass('red');
	} else {
		$this.addClass('green');

	}



}


var cachedMargin = 0; // nimatingToThisMargin
function minCarouselWidth () {
	return -2844; // should be calculated based on the margins, li width, and max age ..
}

var ageWidth = 40;
var carouselWidth = 40;
function SelectAge(age){
	var offset = -80;
	ml = (-(age - min) * ageWidth) + carouselWidth/2 + offset + "px"
	$('.carousel').animate({marginLeft: ml},250);
	
}
