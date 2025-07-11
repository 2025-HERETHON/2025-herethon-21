document.addEventListener('DOMContentLoaded', function () {
  const today = new Date();
  const todayStr = `${today.getFullYear()}-${String(today.getMonth() + 1).padStart(2, "0")}-${String(today.getDate()).padStart(2, "0")}`;

  const aiPredictedSchedules = [
    { start: "2025-07-05", end: "2025-07-10", type: "trip" },
    { start: "2025-07-12", end: "2025-07-14", type: "birthday" },
    { start: "2025-07-16", end: "2025-07-20", type: "exam" },
    { start: "2025-07-22", end: "2025-07-24", type: "date" }
  ];

  const scheduleTypeInfo = {
    trip: { label: "월경기", image: "/static/assets/img/sad_pipi.png" },
    birthday: { label: "난포기", image: "/static/assets/img/happy_pipi.png" },
    exam: { label: "배란기", image: "/static/assets/img/happy_pipi.png" },
    date: { label: "황체기", image: "/static/assets/img/sad_pipi.png" }
  };

  function isDateInRange(dateStr, startStr, endStr) {
    const date = new Date(dateStr);
    const start = new Date(startStr);
    const end = new Date(endStr);
    return date >= start && date <= end;
  }

  const textBox = document.querySelector(".text_box .text_image_wrapper");
  const todaySchedule = aiPredictedSchedules.find(schedule =>
    isDateInRange(todayStr, schedule.start, schedule.end)
  );

  if (textBox) {
    if (todaySchedule && scheduleTypeInfo[todaySchedule.type]) {
      const info = scheduleTypeInfo[todaySchedule.type];
      textBox.innerHTML = `
        <span class="text_1">오늘은 </span>
        <span class="text_2 text_${todaySchedule.type}">${info.label}</span>
        <span class="text_3">입니다</span>
        <img src="${info.image}" alt="${info.label} 이미지" class="cycle_logo" />
      `;
    } else {
      textBox.innerHTML = `
        <span class="text_1">오늘의 주기는 </span>
        <span class="text_2">월경기</span>
        <span class="text_3">입니다</span>
        <img src="/static/assets/img/cycle_logo.png" alt="로고" class="cycle_logo" />
      `;
    }
  }

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
    const thumbWidth = 55;
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
