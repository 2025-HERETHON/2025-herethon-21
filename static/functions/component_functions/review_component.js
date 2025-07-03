document.addEventListener("DOMContentLoaded", function () {
    const stars = document.getElementsByClassName("star_per");
    const savebtn = document.getElementById("savebtn");
    
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
    savebtn.addEventListener("click", function() {
        let answer = confirm("저장하시겠습니까?");
        if (answer) alert("리뷰가 저장되었습니다.");
        else alert("취소되었습니다.")
    })
})
