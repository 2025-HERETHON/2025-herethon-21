document.addEventListener("DOMContentLoaded", function () {
  const scrapbtn = document.getElementById("scrapicon");

  const defaultSrc = scrapbtn.dataset.default;
  const scrapedSrc = scrapbtn.dataset.scraped;

  let isScraped = false;

  scrapbtn.addEventListener("click", function () {
    scrapbtn.src = isScraped ? defaultSrc : scrapedSrc;
    isScraped = !isScraped;
  });
});
