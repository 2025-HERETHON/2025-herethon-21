document.addEventListener('DOMContentLoaded', function () {
  const toggle = document.getElementById('toggleSwitch');
  const startBtn = document.getElementById("start_btn");
  toggle.addEventListener('change', function () {
    if (toggle.checked) {
    window.location.href = "/cyclepage";
  } else {
    window.location.href = "/restpage";
  }
  });

  const slider = document.getElementById("customSlider");
  const fill = document.getElementById("fillTrack");
  const label = document.getElementById("timeLabel");

  const timeValues = ["0m", "10m", "20m", "40m", "60m"];

  function updateSlider() {
    const value = parseInt(slider.value);
    const percent = (value / 4) * 100;
    const sliderWidth = slider.offsetWidth;
    const thumbWidth = 55; // 현재 설정된 버튼 지름
    const trackExtraOffset = thumbWidth / 2;
    const availableWidth = sliderWidth - thumbWidth;

    const thumbCenter = (value / 4) * availableWidth + trackExtraOffset;
    label.style.left = `${thumbCenter - label.offsetWidth / 2}px`;


    fill.style.width = percent + "%";

    if (value === 0) {
      label.style.display = "none";
      slider.classList.remove('user-interacted'); 
      startBtn.disabled = true;
      startBtn.style.backgroundColor = "white";
      startBtn.style.color = "#A48BE7";
      startBtn.style.border = "3px solid #A48BE7";
    } else {
      label.style.display = "block";
      label.textContent = timeValues[value];

      const thumbCenter = (value / 4) * (sliderWidth - thumbWidth) + thumbWidth / 2;
      const labelOffset = thumbCenter / 2 - label.offsetWidth / 2;
      label.style.left = `${labelOffset}px`;
      slider.classList.add('user-interacted');
      
      
      startBtn.disabled = false;
      startBtn.style.backgroundColor = "#A48BE7";
      startBtn.style.color = "white";
      startBtn.style.border = "3px solid #A48BE7";
    }
  }

  slider.addEventListener("input", updateSlider);
  slider.value = 2;
  updateSlider();

  slider.addEventListener('mousedown', () => {
    slider.classList.add('user-interacted');
  });

  slider.addEventListener('touchstart', () => {
    slider.classList.add('user-interacted');
  });
  startBtn.addEventListener("click", function () {
    if (!startBtn.disabled) {
      window.location.href = "/routineingpage";
    }
  });

  const scrapbtn = document.getElementById("scrapicon");
  const border = document.getElementById("border");

  const defaultSrc = scrapbtn.dataset.default;
  const scrapedSrc = scrapbtn.dataset.scraped;

  let isScraped = false;

  scrapbtn.addEventListener("click", function () {
    scrapbtn.src = isScraped ? defaultSrc : scrapedSrc;
    isScraped = !isScraped;
  });
}); 