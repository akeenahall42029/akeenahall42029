$(document).ready(function() {
	//This line of code will change all h1 tags to red when hovered over, and they will return to white once the mouse is no longer hovering over the text
	$('h1').hover(on,off);
		function on (){
		$(this).css("color","red");
		}
		function off(){
		$(this).css("color","white");
		}
	$("#img").hover(enter,leave);
		function enter(){
			this.src = "ombre.jpg";
		}
		function leave(){
			this.src = "computerClassSetup.jpg";
		}


})
