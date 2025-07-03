document.addEventListener("DOMContentLoaded", function () {
    const stars = document.getElementsByClassName("star_per");
    const savebtn = document.getElementById("savebtn");
    const content = document.getElementById("text");
    
    for (let i = 0; i < stars.length; i++) {
    stars[i].addEventListener("click", function () {
        for (let j = 0; j < stars.length; j++) {
        stars[j].style.color = " rgb(202, 202, 202)";
        }
        for (let j = 0; j < i + 1; j++) {
        stars[j].style.color = "pink";
        }
    });
    }
})
