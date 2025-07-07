function changeBgImage() {
  const img = document.getElementById("clickImg");
  const beforeSrc = "/static/assets/img/click_before.png";
  const afterSrc = "/static/assets/img/click_after.png";


  if (img.src.includes('click_before.png')) {
    img.src = afterSrc;
    img.classList.add('large');  // 크기 키우기
  } else {
    img.src = beforeSrc;
    img.classList.remove('large'); // 원래 크기로
  }
}
