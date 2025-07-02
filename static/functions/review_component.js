document.addEventListener("DOMContentLoaded", function () {
    const stars = document.getElementsByClassName("star_per");
    const savebtn = document.getElementById("savebtn");
    const content = document.getElementById("text");
    let cnt = 0;
    for (let i = 0; i < stars.length; i++) {
    stars[i].addEventListener("click", function () {
        for (let j = 0; j < stars.length; j++) {
        stars[j].style.color = " rgb(202, 202, 202)";
        }
        for (let j = 0; j < i + 1; j++) {
        stars[j].style.color = "pink";
        cnt++;
        }
    });
    }
    savebtn.addEventListener("click", function () {
    if (content.value.length === 0) {
        alert("내용을 입력해주세요.");
    } else if (cnt === 0) {
        alert("운동 루틴을 별점으로 평가해주세요.");
    } else {
        alert("저장되었습니다.");
    }
    });
})
