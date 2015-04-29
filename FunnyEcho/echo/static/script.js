/**
 * 
 */

function changed() {
	var inputtext = document.getElementById("inputtext") ;
	// reference to the DOM node of the <input> tag
	
	var text = inputtext.value ;
	
	var outputtext = document.getElementById("outputtext") ;
	
	outputtext.value = text ;
	

}