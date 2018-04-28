$(document).ready(function(){
	// CSS doesn't work for last-child so doing it manually using JQuery. . lol
	$('.item').last().css('margin-bottom','60px')

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
//
//
		$('#pre-assessment .acknowledgement .checkbox').on('click',function(){
			if ($(this).hasClass('checked')){
				$(this).removeClass('checked');
			} else {
				$(this).addClass('checked');
			}
		})

		// Submit form
		$('#pre-assessment .sendButton').on('click',function(){
			SubmitForm();
			console.log("This question is required.");
			// use jquery to extract data from each selection
			// Clear prev errors
			// This question is required error inject
			// Assemble JS object
			// Post to Google web form eg https://medium.com/@dmccoy/how-to-submit-an-html-form-to-google-sheets-without-google-forms-b833952cc175
		});
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

	// Set the hidden input value to the value the user selected.
	console.log('prev val:'+	$this.closest('.item').find(".hidden_form_field").val());
	$this.closest('.item').find(".hidden_form_field").val($this.text());
	console.log('new val:'+	$this.closest('.item').find(".hidden_form_field").val());




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
	$('#age_hidden').val(age);
	
}

var UserInputData = {
	GetFormFieldData : function( formFieldId){
		console.log('checking:'+formFieldId);
		var $el = $("[form_field_id='"+formFieldId+"']");
		var val = 	$el.val();
		if (val.length == 0){
			this.AppendError($el,formFieldId);
			if (!errorDueToFieldNotFilled) {
				// Only scroll to the first error message.
				$(window).scrollTop($('.errorMessage').offset()['top'] - 150); // snap the window to the error.
			}	
			errorDueToFieldNotFilled = true;
		}
		return val;
	}, 
	AppendError : function($el,formFieldId){
		$el.after("<div class='errorMessage'>"+formFieldId+": This field is required.</div>");
		$('.errorMessage').animate({backgroundColor : "#f0f"}, 2000 ); 
	
	},
	ClearErrors : function(){
		$('.errorMessage').each(function(){
			$(this).remove();
		});
	}
	
}

function JsonToGet(data){
	var serialized = ""
	for (var key in data){
		serialized += key + "=" + data[key].toString() + "&";
	}
	return serialized;
	
}

var errorDueToFieldNotFilled = false;

function SubmitForm(){
	var url = 'https://script.google.com/macros/s/AKfycbxcPtvV8Fze6MAnPunc4m6jL0dvSoR-jqINBekVRTKNfFR_l5M/exec';
	errorDueToFieldNotFilled = false;
	UserInputData.ClearErrors();
	data = {};
	userInputDataFields = [
		'Organization',
		'genderPositive',
	]
	for (i in userInputDataFields){
		var field = userInputDataFields[i];
		data[field] = UserInputData.GetFormFieldData(field);
		if (errorDueToFieldNotFilled) {
			return false;
		}
	}

	var serialized = JsonToGet(data);

	// Post the data to google forms.
	var jqxhr = $.ajax({
		url: url,
		method: "GET",
		dataType: "json",
		data: serialized,
	  }).success(function(){
		console.log("hha");
		// do something

		});
}


