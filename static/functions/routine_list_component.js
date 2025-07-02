document.addEventListener("DOMContentLoaded", function () {
    const scrapbtn = document.getElementsByTagName("img")[0];
    let isScraped = false;

    scrapbtn.addEventListener("click", function () {
    if (isScraped) {
        scrapbtn.src = ".{% static 'assets/img/scrapicon.png' %}";
    } else {
        scrapbtn.src = "{% static 'assets/img/scrapicon_scraped.png' %}";
    }
    isScraped = !isScraped;
    });
})
