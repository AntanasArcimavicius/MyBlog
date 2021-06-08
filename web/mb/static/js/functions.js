const nav = document.querySelector("#myNav");
const navTop = document.querySelector(".nav-top");
const aboutSection = document.querySelector(".about-section");
const emailModal = document.querySelector(".email-modal");
const profileImg = document.querySelector("#profile-photo");
const closeButton = document.querySelector(".close");

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
    }
} );

document.querySelector(".open-email").addEventListener("click", function() {
    emailModal.style.display = "flex";
    profileImg.style.display = "none";
    nav.className = "navbar";
    closeButton.style.zIndex = 30;
    console.log("working")
});

closeButton.addEventListener("click", function() {
    emailModal.style.display = "none";
    profileImg.style.display = "inline-block";
    closeButton.style.zIndex = 0;
});