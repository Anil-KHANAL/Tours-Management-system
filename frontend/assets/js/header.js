const menu_icon = document.getElementById('menu-icon');
const nav = document.getElementById('nav');
const nav_close_icon = document.getElementById('nav-close');
const social_icons = document.getElementById('social-icons');

const header = document.querySelector('header');
const banner = document.querySelector('.header-mark');

let options = {
	// rootMargin:'-100px'
};

let observer = new IntersectionObserver(function (entries, observer) {
	entries.forEach((entry) => {
		if (!entry.isIntersecting) {
			header.classList.add('sticky');
		} else {
			header.classList.remove('sticky');
		}
	});
}, options);

observer.observe(banner);

menu_icon.addEventListener('click', () => {
	nav.classList.add('show');
});

nav_close_icon.addEventListener('click', () => {
	nav.classList.remove('show');
});
