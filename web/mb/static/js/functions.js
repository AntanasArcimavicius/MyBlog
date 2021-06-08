const nav = document.querySelector("#myNav");
const navTop = document.querySelector(".nav-top")
const aboutSection = document.querySelector(".about-section")
const email_modal = document.querySelector(".email-modal")
const profile_img = document.querySelector("#profile-photo")

function openNav() {
    nav.classList.toggle("opened");
    navTop.classList.toggle("clearfix")
}

function scrollToAbout() {
    aboutSection.scrollIntoView(true);
    nav.className = "navbar";
}

document.body.addEventListener("click", function(event) {
    if (!nav.contains(event.target)) {
        nav.className = "navbar";
    }
} );

document.querySelector(".open-email").addEventListener("click", function() {
    email_modal.style.display = "flex";
    profile_img.style.display = "none";
    nav.className = "navbar";
});

document.querySelector(".close").addEventListener("click", function() {
    email_modal.style.display = "none";
    profile_img.style.display = "inline-block";
});