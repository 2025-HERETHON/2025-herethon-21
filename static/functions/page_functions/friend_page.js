function changeBgImage() {
  const img = document.getElementById("clickImg");
  const beforeSrc = "/static/assets/img/click_before.png";
  const afterSrc = "/static/assets/img/click_after.png";
  

  if (img.src.includes('click_before.png')) {
    img.src = afterSrc;
    img.classList.add('large');  
  } else {
    img.src = beforeSrc;
    img.classList.remove('large'); 
  }
}
