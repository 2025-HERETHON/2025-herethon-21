document.addEventListener("DOMContentLoaded", function () {
  const scrapIcon = document.getElementById("scrapicon");
  const border = document.getElementById("border");
  const scrapTextBtn = document.getElementById("scrap_btn"); // 하단 버튼

  const defaultSrc = scrapIcon.dataset.default;
  const scrapedSrc = scrapIcon.dataset.scraped;

  let isScraped = false;

  // ✅ 초기 스타일 적용
  scrapIcon.src = defaultSrc;
  border.style.border = "2px solid rgb(223, 223, 223)";
  scrapTextBtn.style.color = "black";
  scrapTextBtn.style.backgroundColor = "white";

  function toggleScrap() {
    isScraped = !isScraped;

    // 아이콘 버튼 스타일
    scrapIcon.src = isScraped ? scrapedSrc : defaultSrc;
    border.style.border = isScraped
      ? "2px solid #A48BE7"
      : "2px solid rgb(223, 223, 223)";

    // 하단 텍스트 버튼 스타일
    scrapTextBtn.style.color = isScraped ? "white" : "black";
    scrapTextBtn.style.backgroundColor = isScraped ? "#A48BE7" : "white";
  }

  scrapIcon.addEventListener("click", toggleScrap);
  scrapTextBtn.addEventListener("click", toggleScrap);
});
