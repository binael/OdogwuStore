$(document).ready(function() {
	// Cache the original text for later use
	let originalText = $("#username").text();

	// On hover, replace the text content
	$("#username").hover(
		function() {
			// Mouseover event
			$(this).text("EDIT PROFILE");
		},
		function() {
			// Mouseout event
			$(this).text(originalText);
		}
	);

	// Click event for the first box
	$('.help').on('click', function () {
		$('.dropdown').toggle(); // Toggle the display of the second box
	});

	// Click event for the document (outside of the boxes)
	$(document).on('click', function (event) {
		// Check if the click is not on the first or second box
		if (!$(event.target).closest('.help, .dropdown').length) {
			$('.dropdown').hide(); // Hide the second box
		}
	});
});
