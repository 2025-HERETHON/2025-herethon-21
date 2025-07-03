document.addEventListener("DOMContentLoaded", function () {
    const conditions = document.getElementsByClassName("condition_per");
    const savebtn = document.getElementById("savebtn");
    const content = document.getElementById("text");

    for (let i = 0; i < conditions.length; i++) {
    conditions[i].addEventListener("click", function () {
        for (let j = 0; j < conditions.length; j++) {
        conditions[j].classList.remove("selected");
        }
        this.classList.add("selected");
    });
    }
})