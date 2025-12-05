const slider = document.getElementsByClassName('slider')[0];
function prev() {

    slider.scrollBy({ left: -300, behavior: 'smooth' })
}
function next() {

    slider.scrollBy({ left: 300, behavior: 'smooth' })
}

const toggle = document.getElementById('menu-toggle');
const mobileMenu = document.getElementById('mobile-menu');

toggle.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
});