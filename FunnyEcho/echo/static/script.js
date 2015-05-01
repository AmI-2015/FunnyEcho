// Register event handlers when is page is ready (han been loaded, and DOM is complete)
$(document).ready(function() {

	// this code is executed when the inline function is called
	// i.e., when the 'ready' event if fired by the document object

	// register handler on the input text
	$('#inputtext').keyup(function() {

		// this code is run at key-up event in the input text cell

		// Query the HTML page for reading user-entered information
		var text = $('#inputtext').val();

		// prepare a Javascript object holding the data that we
		// need to send to the server (the request parameters)
		var requestdata = {
			'text' : text,
			'reverse' : $('#reverseBox').prop("checked"),
			'flip' : $('#flipBox').prop("checked")
		};

		// Launch the request to the server
		// See: http://api.jquery.com/jQuery.ajax/
		$.ajax({
			// remote URL and method type (for transferring JSON, always use
			// POST)
			url : '/process',
			type : 'POST',

			// Provide correct Content-Type, so that Flask will know how to
			// process it.
			contentType : 'application/json',
			// Encode data as JSON. Data will be stored in the Http POST Request
			// Body.
			data : JSON.stringify(requestdata),

			// This is the type of data expected back from the server.
			// With this information, jQuery will already decode the response
			// for us
			dataType : 'json',

			// The function that will be called when the respose returns
			// The parameter 'ret' holds the data (response body), interpreted
			// according
			// to the 'dataType' that we set (i.e., a JS object created from
			// JSON)
			success : function(ret) {
				// this code is run after the response is received

				// may use the 'ret' object to extract info from the response
				$('#outputtext').val(ret['text']);
			} // end of success function

		}); // end of .ajax call

		// nothing more to do, now... the request is on its way, and
		// we must wait untilt the response arrives (and the 'success' function
		// is called
		
	}); // end of keyup event handler function

}); // end of document ready event handler function
