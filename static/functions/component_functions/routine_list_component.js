document.addEventListener("DOMContentLoaded", function () {
  const scrapIcon = document.getElementById("scrapicon");
  const border = document.getElementById("border");
  const scrapTextBtn = document.getElementById("scrap_btn"); // 하단 버튼

  const defaultSrc = scrapIcon.dataset.default;
  const scrapedSrc = scrapIcon.dataset.scraped;

  let isScraped = false;

  function toggleScrap() {
    isScraped = !isScraped;

    // 아이콘 버튼 스타일
    scrapIcon.src = isScraped ? scrapedSrc : defaultSrc;
    border.style.border = isScraped
      ? "3px solid #A48BE7"
      : "3px solid rgb(223, 223, 223)";

    // 하단 텍스트 버튼 스타일
    scrapTextBtn.style.color = isScraped ? "white" : "#A48BE7";
    scrapTextBtn.style.backgroundColor = isScraped ? "#A48BE7" : "white";

  }

  // 두 버튼에 이벤트 리스너 연결
  scrapIcon.addEventListener("click", toggleScrap);
  scrapTextBtn.addEventListener("click", toggleScrap);
});
