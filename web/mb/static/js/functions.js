const body = document.body
const nav = document.querySelector("#myNav");
const navTop = document.querySelector(".nav-top")
const aboutSection = document.querySelector(".about-section")

function openNav() {
    nav.classList.toggle("opened");
    navTop.classList.toggle("clearfix")
}

function scrollToAbout() {
    aboutSection.scrollIntoView({behavior: "smooth", block: "end", inline: "nearest"});
    nav.className = "navbar";
}

body.addEventListener("click", function(event) {
    if (!nav.contains(event.target)) {
        nav.className = "navbar";
    }
} );