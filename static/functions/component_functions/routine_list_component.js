document.addEventListener("DOMContentLoaded", function () {
  const scrapbtn = document.getElementById("scrapicon");
  const border = document.getElementById("border");

  const defaultSrc = scrapbtn.dataset.default;
  const scrapedSrc = scrapbtn.dataset.scraped;

  let isScraped = false;

  scrapbtn.addEventListener("click", function () {
    scrapbtn.src = isScraped ? defaultSrc : scrapedSrc;
    border.style.border = isScraped ? "2px solid rgb(223, 223, 223)" : "2px solid rgb(174, 129, 218)";
    isScraped = !isScraped;
  });
});
