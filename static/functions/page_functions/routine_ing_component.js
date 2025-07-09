document.addEventListener("DOMContentLoaded", function () {
  const stepElements = document.querySelectorAll(".step");
  const radius = 30;
  const strokeWidth = 7;

  const stepContentEl = document.getElementById("step_content");
  const stepCategoryEl = document.getElementById("category");
  const routineImage = document.getElementById("routine_image");
  const stepNumber = document.getElementById("step_number");
  const prevBtn = document.getElementById("photo_prev");
  const nextBtn = document.getElementById("photo_next");
  const starscoreEl = document.querySelector(".starscore");

  function updateStars(difficulty) {
    let starsHTML = "";
    for (let i = 1; i <= 5; i++) {
      if (i <= difficulty) {
        starsHTML += `<span class="star_per">
          <img src="/static/assets/img/star_purple.png" alt="보라별" />
        </span>`;
      } else {
        starsHTML += `<span class="star_per">
          <img src="/static/assets/img/star_gray.png" alt="회색별" />
        </span>`;
      }
    }
    starscoreEl.innerHTML = starsHTML;
  }


  let currentImageIndex = 0;
  let currentStepIndex = 0;

  function injectProgressCircle(circleEl, durationMin) {
    const svgSize = 80;
    const radius = 30;
    const strokeWidth =7;
    const center = svgSize / 2;
    const circumference = 2 * Math.PI * radius;

    // SVG 구조 구성
    circleEl.innerHTML = `
      <svg width="${svgSize}" height="${svgSize}" style="transform: rotate(90deg) scale(-1,1); overflow: visible">
        <defs>
          <linearGradient id="purpleGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#A48BE7"/>
            <stop offset="100%" stop-color="#E0CFFF"/>
          </linearGradient>
        </defs>

        <!-- 배경 원 -->
        <circle cx="${center}" cy="${center}" r="${radius}"
          stroke="#eee" stroke-width="${strokeWidth}" fill="none" />

        <!-- 진행 원 -->
        <circle class="progress" cx="${center}" cy="${center}" r="${radius}"
          stroke="url(#purpleGradient)"
          stroke-width="${strokeWidth}" fill="none"
          stroke-dasharray="${circumference}"
          stroke-dashoffset="${circumference}"
          stroke-linecap="round"
        />


      <div class="time-text">${durationMin}m</div>
    `;

    // 텍스트 중앙 정렬
    const timeText = circleEl.querySelector(".time-text");
    Object.assign(timeText.style, {
      position: "absolute",
      top: "50%",
      left: "50%",
      transform: "translate(-50%, -50%)",
      fontWeight: "bold",
      fontSize: "16px",
      textAlign: "center",
      lineHeight: "1",
    });

    circleEl.style.position = "relative";
  }


  function updateImage() {
    const detailImages = routineData[currentStepIndex].detail_images;
    const imagePath = detailImages[currentImageIndex];

    routineImage.src = "/static/" + imagePath;
    stepNumber.textContent = currentImageIndex + 1;

    prevBtn.style.display = currentImageIndex === 0 ? "none" : "block";
    nextBtn.style.display = currentImageIndex === detailImages.length - 1 ? "none" : "block";
  }

  function runTimer(index) {
    if (index >= stepElements.length) {
      window.location.href = "/finishedroutine";
      return;
    }

    currentStepIndex = index;
    currentImageIndex = 0;
    updateImage();

    const step = stepElements[index];
    const circleEl = step.querySelector(".circle");
    const durationMin = durations[index];
    const durationSec = durationMin * 60;

    stepContentEl.textContent = routineData[index].content;
    stepCategoryEl.textContent = routineData[index].category;
    updateStars(routineData[index].difficulty);

    injectProgressCircle(circleEl, durationMin);

    const progressCircle = circleEl.querySelector(".progress");
    const timeText = circleEl.querySelector(".time-text");
    const circumference = 2 * Math.PI * radius;

    let elapsed = 0;
    const timer = setInterval(() => {
      elapsed++;
      const ratio = elapsed / durationSec;
      const offset = circumference * (1 - ratio);
      progressCircle.style.strokeDashoffset = offset;

      // 버블 위치 계산
      const angle = 360 * ratio;
      const rad = (angle - 90) * (Math.PI / 180);

      timeText.textContent = `${Math.ceil((durationSec - elapsed) / 60)}m`;

      if (elapsed >= durationSec) {
        clearInterval(timer);
        timeText.textContent = "완료!";
        timeText.style.width= "50px";
        runTimer(index + 1);
      }
    }, 1000);

  }

  prevBtn.addEventListener("click", () => {
    const detailImages = routineData[currentStepIndex].detail_images;
    if (currentImageIndex > 0) {
      currentImageIndex--;
      updateImage();
    }
  });

  nextBtn.addEventListener("click", () => {
    const detailImages = routineData[currentStepIndex].detail_images;
    if (currentImageIndex < detailImages.length - 1) {
      currentImageIndex++;
      updateImage();
    }
  });

  runTimer(0);
});
