function openForm() {
	let form_book = document.querySelector('.form_book');
	let btn_book = document.querySelector('.btn_book');
	let actualDisplay = getComputedStyle(form_book).display;
	if (actualDisplay == 'none') {
    	form_book.style.display = 'block';
    	btn_book.textContent = 'Отмена';
    	btn_book.style.background = '#dc3545';
  	}
  	else {
  		form_book.style.display = 'none';
  		btn_book.textContent = 'Добавить книгу';
  		btn_book.style.background = '';
  	}
  	window.scrollTo(0, 150);
}

function openForm2() {
	let form_course = document.querySelector('.form_course');
	let btn_course = document.querySelector('.btn_course');
	let actualDisplay = getComputedStyle(form_course).display;
	if (actualDisplay == 'none') {
    	form_course.style.display = 'block';
    	btn_course.textContent = 'Отмена';
  	}
  	else {
  		form_course.style.display = 'none';
  		btn_course.textContent = 'Добавить курс';
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
	if (btn_redact.textContent == 'Редактировать') {
		btn_redact.textContent = 'Отмена';
		btn_redact.style.background = '#dc3545';
		for (let post of delete_posts) {
			let actualDisplay = getComputedStyle(post).display;
	    	if (actualDisplay == 'none') {
	    		post.style.display = 'table-cell';
	  		}
	  	}
	} else {
		btn_redact.textContent = 'Редактировать';
		btn_redact.style.background = '';
		for (let post of delete_posts) {
			let actualDisplay = getComputedStyle(post).display;
	    	if (actualDisplay == 'table-cell') {
	    		post.style.display = 'none';
	  		}
	  	}
	}
}