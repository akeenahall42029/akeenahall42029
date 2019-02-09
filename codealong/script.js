//This line of code adds a paragraph, but it doesn't have anything in it. You can think of it as doing this in HTML, <p> </p>// 
var paragraph = document.createElement("p");
// This line of code writes something into the new paragraph we just created in this file// 
paragraph.innerHTML = "You can take me to get fried chicken";
var videoBanner = document.getElementById("videoBanner");//This name doesn't mean anything special, it's just the name of the id in HTML// 
videoBanner.appendChild(paragraph);
//This code will add 'Ladies and Gentlemen' before the added 'You can take me to get fried chicken'//
var newHeader = document.createElement('h2');
newHeader.innerHTML = "Ladies and Gentlemen";
videoBanner.insertBefore(newHeader,paragraph);

//This will remove the new header 'Ladies and Gentlemen' and 'You can take me to get fried chicken'// 

videoBanner.removeChild(paragraph);
videoBanner.removeChild(newHeader);
//adding an event 
videoBanner.addEventListener("click", myEventHandler);
function myEventHandler(){
	alert("hey, buy me some sushi");
}