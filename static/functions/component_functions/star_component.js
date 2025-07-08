document.addEventListener("DOMContentLoaded", function () {
  const stars = document.getElementsByClassName("star_per");
  const filledSrc = "/static/assets/img/star_purple.png";
  const emptySrc = "/static/assets/img/star_gray.png";

  for (let i = 0; i < stars.length; i++) {
    stars[i].addEventListener("click", function () {
      for (let j = 0; j < stars.length; j++) {
        stars[j].querySelector("img").src = emptySrc;
      }
      for (let j = 0; j <= i; j++) {
        stars[j].querySelector("img").src = filledSrc;
      }
    });
  }
});
