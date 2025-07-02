document.addEventListener("DOMContentLoaded", function () {
    const conditions = document.getElementsByClassName("condition_per");
    const savebtn = document.getElementById("savebtn");
    const content = document.getElementById("text");
    let cnt = 0;
    for (let i = 0; i < conditions.length; i++) {
    conditions[i].addEventListener("click", function () {
        for (let j = 0; j < conditions.length; j++) {
        conditions[j].classList.remove("selected");
        }
        this.classList.add("selected");
        cnt++;
    });
    }
    savebtn.addEventListener("click", function () {
    if (content.value.length === 0) {
        alert("내용을 입력해주세요.");
    } else if (cnt === 0) {
        alert("오늘의 감정을 선택해주세요.");
    } else {
        alert("저장되었습니다.");
    }
    });
})