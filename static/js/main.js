function openForm() {
	let form_book = document.querySelector('.form_book');
	let btn_book = document.querySelector('.btn_book');
	let actualDisplay = getComputedStyle(form_book).display;
	if (actualDisplay == 'none') {
    	form_book.style.display = 'block';
    	btn_book.style.display = 'none';
  	}
}
function openForm2() {
	let form_course = document.querySelector('.form_course');
	let btn_course = document.querySelector('.btn_course');
	let actualDisplay = getComputedStyle(form_course).display;
	if (actualDisplay == 'none') {
    	form_course.style.display = 'block';
    	btn_course.style.display = 'none';
  	}
}