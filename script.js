
// slideshow; taking code from w3Schools
var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
}
//
$(document).ready(function() {
	//This line of code will change all h1 tags to red when hovered over, and they will return to white once the mouse is no longer hovering over the text
	$('h1').hover(on,off);
		function on (){
		$(this).css("color","red");
		}
		function off(){
		$(this).css("color","white");
		}
	//this code will make the divs, about me, contact, etc, toggle down and back up 
	$('#aboutMeButton').click(function(){
		$('#about').slideToggle("slow");
	});
	$('#experienceB').click(function(){
		$('#experience').slideToggle("slow");
	});
	$('#projectb').click(function(){
		$('#projects').slideToggle("slow");

	});
})




