const nav = document.querySelector("#myNav");
const navTop = document.querySelector(".nav-top");
const aboutSection = document.querySelector(".about-section");
const emailModal = document.querySelector(".email-modal");
const profileImg = document.querySelector("#profile-photo");
const closeButton = document.querySelector(".close");
const header = document.querySelector(".header")

function openNav() {
    nav.classList.toggle("opened");
    navTop.classList.toggle("clearfix");
}

function scrollToAbout() {
    aboutSection.scrollIntoView(true);
    nav.className = "navbar";
}

document.body.addEventListener("click", function(event) {
    if (!nav.contains(event.target)) {
        nav.className = "navbar";
        navTop.classList.remove("clearfix");
    }
} );

document.querySelector(".open-email").addEventListener("click", function() {
    emailModal.style.display = "flex";
    profileImg.style.display = "none";
    nav.className = "navbar";
    header.style.zIndex = 0;
    closeButton.style.zIndex = 30;
});

closeButton.addEventListener("click", function() {
    emailModal.style.display = "none";
    profileImg.style.display = "inline-block";
    header.style.zIndex = 10;
    closeButton.style.zIndex = 0;
});