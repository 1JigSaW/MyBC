function openForm() {
	let form_book = document.querySelector('.form_book');
	let btn_book = document.querySelector('.btn_book');
	let actualDisplay = getComputedStyle(form_book).display;
	if (actualDisplay == 'none') {
    	form_book.style.display = 'block';
    	btn_book.style.display = 'none';
  	}
  	window.scrollTo(0, 150);
}

function openForm2() {
	let form_course = document.querySelector('.form_course');
	let btn_course = document.querySelector('.btn_course');
	let actualDisplay = getComputedStyle(form_course).display;
	if (actualDisplay == 'none') {
    	form_course.style.display = 'block';
    	btn_course.style.display = 'none';
  	}
  	window.scrollTo(0, 1000);
}

$( function()
	{
		$( "#datepicker_2" ).datepicker();
		$( "#datepicker" ).datepicker();
});

function redact() {
	let delete_posts = document.querySelectorAll('.delete_post');
	let btn_redact = document.querySelector('.btn_redact');
	for (let post of delete_posts) {
		let actualDisplay = getComputedStyle(post).display;
    	if (actualDisplay == 'none') {
    		post.style.display = 'block';
  		}
  	}
}