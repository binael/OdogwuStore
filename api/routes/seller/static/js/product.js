$(document).ready(function () {
	$('.image-file').on('click', function () {
		$('.image-data').click();
	});

	$('.edit-form').click(function () {
		toggleEditMode($(this));
	});

	function toggleEditMode (element) {
		let form = element.closest('.detail-name').find('.form-control');
		let input = form

		if ($(element).text() === "EDIT") {
			$(element).text("SAVE");
			input.prop("readonly", false);
			form.addClass("change-form");

		} else {
			$(element).text("EDIT");
			input.prop("readonly", true);
			form.removeClass("change-form");
		};
	};

	$('.aux-title').click(function () {
		$('.aux-title').removeClass('selected');
		$(this).addClass('selected');
		$('.info').hide();

		let pageId = $(this).data("page");
		$("#" + pageId).show();
	});
});
