$(document).ready(function(){
	// CSS doesn't work for last-child so doing it manually using JQuery. . lol
	$('.item').last().css('margin-bottom','60px')

	// When you click on "name" or "organization" it should select the existing text (if any)
	$('input').on('click',function(){
		$(this).focus();
		$(this).select();
	});


	// Age
	min=18;
	max=99;
	carouselWidth = $('.carousel_container').width();
	for(i=min;i<max;i++){
		if (i == 31) {
//			SelectAge(31,false); // initiate the age carousel to age 31, but pass "false" so that the hidden field isn't filled.
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
		UserInputData.UpdateHiddenField('Gender',$(this).text());
	});


	// Sexual Orientation
	$('.sexual-orientation ul li').click(function(){
		$('.sexual-orientation ul li').each(function(){
			$(this).removeClass('selected');
		});
		$(this).addClass('selected');
		UserInputData.UpdateHiddenField('Sexual_Orientation',$(this).text());
	});


	

	// Pre Assessment

	// Some questions will show or hide subsequent questions depending on your answer.
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
				$(div).fadeIn();	
			} else {
				$(div).fadeOut();	
			}
		}
		

	});


	// Detect clicks on either scale [1,2,3,4,5] or dynamic [YES,NO,Kind of] options
	$('.square').on('click',function(){ 
		Clicked($(this),'.square');
		return;
	});
	$('.dynamic').on('click',function(){ 
		Clicked($(this),'.dynamic');
		return;
	});

	// Acknowledgement
	$('#pre-assessment .acknowledgement .checkbox').on('click',function(){
		if ($(this).hasClass('checked')){
			$(this).removeClass('checked');
			$("[form_field_id='acknowledgement']").val("");
		} else {
			$(this).addClass('checked');
			$("[form_field_id='acknowledgement']").val("checked");
		}
	})

	// Submit form
	$('#pre-assessment .sendButton').on('click',function(){
		SubmitForm();
		// followed this method: 
		// https://medium.com/@dmccoy/how-to-submit-an-html-form-to-google-sheets-without-google-forms-b833952cc175
	});
});

function Clicked($this, el){
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
	$this.closest('.item').find(".hidden_form_field").val($this.text());
}

// Age
var cachedMargin = 0; // animatingToThisMargin
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
	UpdateHiddenField : function(formFieldId, newValue){
		var $el = $("[form_field_id='"+formFieldId+"']");
		$el.val(newValue);
	},

	GetFormFieldData : function( formFieldId){
//		console.log('checking:'+formFieldId);
		var $el = $("[form_field_id='"+formFieldId+"']");
		var val = 	$el.val();
		if (val.length == 0 && $el.attr("data-required") == "true"){
			this.AppendError($el,formFieldId);
			if (!errorDueToFieldNotFilled) {
				// Only scroll to the first error message. Remove this if to show ALL error messages at once (can be lots of red)
				var errorOffset = 250;
				$(window).scrollTop($('.errorMessage').offset()['top'] - errorOffset); // snap the window to the error.
			}	
			errorDueToFieldNotFilled = true;
		}
		return val;
	}, 
	AppendError : function($el,formFieldId){
		$el.after("<div class='errorMessage'>This field is required.</div>");
		$('.errorMessage').animate({backgroundColor : "#f0f"}, 2000 ); 
	
	},
	ClearErrors : function(){
		$('.errorMessage').each(function(){
			$(this).remove();
		});
	}
	
}

function SerializeJson(data){
	var serialized = ""
	for (var key in data){
		serialized += key + "=" + data[key].toString() + "&";
	}
	return serialized;
	
}

var errorDueToFieldNotFilled = false; // clumsy way to detect error ..
var submitting = false; // prevent multiple submit
function SubmitForm(){
	if (submitting) {
		console.log('form submit clicked after already being submitted');
		return;
	}
	errorDueToFieldNotFilled = false;
	UserInputData.ClearErrors();
	data = {};
	dataFields.push.apply(dataFields, form_field_ids.split(','));	
	dataFields.push('acknowledgement');
	dataFields.push('sessionId');
	for (i in dataFields){
		var field = dataFields[i];
		data[field] = UserInputData.GetFormFieldData(field);
		
		if (errorDueToFieldNotFilled) {
//			console.log('%c error: not filled '+field,'color:red');
			return false;
		} else {
//			console.log('%c filled '+field+' with '+data[field],'color:blue');

		}
	}
	data["sheetName"] = sheetName;

	// All "required" form_fill_id elements were completed.
	// Before making the query to google sheets, indicate to user that form is being submitted.
	
	submitting = true;
	LoadingFx();

	// Serialize the json object we constructed from user inputs for a GET request to Google Sheets
	var serialized = SerializeJson(data);
	
	// Post the data to google forms.
	var jqxhr = $.ajax({
		url: url,
		method: "GET",
		dataType: "json",
		data: serialized,
	  }).success(function(){
		// If Unity, make sure this lets the new location text be captured by the Browser.OnUrlLoaded function
		// So that user may continue.
		//
		//	For daydream, actually take them to next page. (could be same?)		
		window.location = completedUrl;

	});
}

function LoadingFx(){
	$('#pre-assessment .sendButton')
		.text('') 
		.css('background-color','white')
		.css('background-position','center')
		.css('background-size','50%')
		.css('background-repeat','no-repeat')
		.css('background-image','url("/static/img/loading.gif")')
		.animate({'background-size':"17%"},420);
}

 
