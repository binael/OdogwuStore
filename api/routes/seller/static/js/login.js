$(document).ready(function () {
	$('#toggle-password').click(function () {
		let passwordField = $('#password');
		let passwordFieldType = passwordField.attr('type');

		if (passwordFieldType === 'password') {
			passwordField.attr('type', 'text');
			$(this).text('HIDE');
		} else {
			passwordField.attr('type', 'password');
			$(this).text('SHOW');
		};
	});
});
