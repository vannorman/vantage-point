
// Detects user resizing browser window and scales canvas to always fit
$(window).resize(function(){
	ResizeGameWindow();
});


// This changes the CSS width and height dimensions of the canvas, which changes the total resolution sent to graphics card
// This should allow the game window to expand or contract with the user's browser without any ill effects with mouse position
function ResizeGameWindow(){
//	if (swapped) return;
//
	if (($(window).height() - 60) / $(window).width() < 576/1024) {
		// pillarbox
		$('#gameContainer').css('height','calc(100% - 60)');
		$('#gameContainer').css('width',$('#gameContainer').height() * 1024 / 576 + "px");	
	} else {
		$('#gameContainer').css('width','100%');
		$('#gameContainer').css('height',$('#gameContainer').width() * 576 / 1024 + "px"); 

	}
	return;


	// The code below (until the next 'return') resizes the canvas to 1024 x 576 or smaller if the window size is smaller.
	var topBarOffset = 60;
	var h = window.innerHeight - topBarOffset;
	var w = window.innerWidth;
	var resX = 1024;
	var resY = 576;
	var widthOffset = resX / 24;
	var heightOffset = resY / 24;
	var ww = 0;
	var hh = 0;
	//var canvas = frames[0].document.getElementById('canvas');
	var canvas = document.getElementById('canvas');
	if ((w / h) > 1.81){ // I do'nt know why this is .75
		ww = (window.innerHeight * resX/resY); 
		heightOffset += resY / 16;
		widthOffset += resX / 16;
		// console.log('a:'+w/h);
	} else {
		ww = window.innerWidth + widthOffset;
		// console.log('b'+w/h);
	}
	var targetWidth = Math.min(ww - widthOffset,1024);
	var targetHeight = (ww / resX * resY - heightOffset); 
	targetHeight = targetWidth / resX * resY;
	$('#gameContainer').css('width',(targetWidth).toString() + 'px');
	$('#gameContainer').css('height',targetHeight.toString() + 'px');	

	return;
	// TODO: use webkit transform so the game runs faster in BIG windows.
	var hh = ww / resX * resY - heightOffset;
	var x = www / 1024;
	var y = hh / 560;
	$('#gameContainer').css('-webkit-transform-origin', '0 0 0');
	$('#gameContainer').css('-webkit-transform','scale3d('+x+','+y+', 1.0)');
	return;
	
//	if (ww > 1000{
	if (false){
		ww /= 2;
		hh /= 2;
		$('#gameContainer').css('-webkit-transform', 'scale3d(2.0, 2.0, 1.0)'); // this line "stretches" the canvas, appearing larger to the user but not requiring more rendering horsepower from the graphics card. Will result in obvious pixelation without much anti-aliasing or other edge improvement fx.
		$('#gameContainer').css('-webkit-transform-origin', '0 0 0'); 
	} else {
		$('#gameContainer').css('-webkit-transform', 'scale3d(1.0, 1.0, 1.0)');

	}
	// https://webglfundamentals.org/webgl/lessons/webgl-2d-scale.html
	// webgl canvas resize and scale doc: http://webglfundamentals.org/webgl/lessons/webgl-resizing-the-canvas.html
}

var swapped = false;
function Swap(amt){
	amt = parseInt(amt);
	console.log('amt:'+amt+',amt/2:'+amt%2);
	swapped = true;
	var targetWidth = swapped % 2 == 0 ? 1024 : 1024/2;
	var targetHeight = swapped % 2 == 0 ? 576 : 576/2;
	$('#gameContainer').css('width',(targetWidth).toString() + 'px');
	$('#gameContainer').css('height',targetHeight.toString() + 'px');	
	if (amt % 2 == 1){
		$('#gameContainer').css('-webkit-transform', 'scale3d(2.0, 2.0, 1.0)');
	} else {
		$('#gameContainer').css('-webkit-transform', 'scale3d(1.0, 1.0, 1.0)'); 
	}
	$('#gameContainer').css('-webkit-transform-origin', '0 0 0'); 
}


