const text_element = document.getElementById('search-title');
let i = 0;
let text = 'S';

setInterval(changeText, 500);

function changeText() {
	let text_add = 'earch Hotels';
	text += text_add[i];
	i++;
	text_element.innerText = text;
	if (text == 'S' + text_add) {
		text = 'S';
		i = 0;
	}
}
