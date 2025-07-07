document.addEventListener("DOMContentLoaded", function () {
  const stepElements = document.querySelectorAll(".step");
  const radius = 30;
  const strokeWidth = 6;

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
    const svgSize = 60;
    const center = svgSize / 2;
    const circumference = 2 * Math.PI * radius;

    circleEl.innerHTML = `
      <svg width="${svgSize}" height="${svgSize}" style="transform: rotate(-90deg); overflow:visible">
        <circle cx="${center}" cy="${center}" r="${radius}" stroke="#e0e0e0" stroke-width="${strokeWidth}" fill="none"/>
        <circle class="progress" cx="${center}" cy="${center}" r="${radius}"
          stroke-width="${strokeWidth}" fill="none"
          stroke-dasharray="${circumference}"
          stroke-dashoffset="${circumference}"
          stroke-linecap="round"
        />
      </svg>
      <div class="time-text">${durationMin}m</div>
    `;

    const timeText = circleEl.querySelector(".time-text");
    Object.assign(timeText.style, {
      position: "absolute",
      top: "50%",
      left: "50%",
      transform: "translate(-50%, -50%)",
      fontWeight: "bold",
      fontSize: "14px",
      lineHeight: "1",
      whiteSpace: "nowrap",
      textAlign: "center",
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
      alert("운동이 모두 완료되었습니다!");
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
      timeText.textContent = `${Math.ceil((durationSec - elapsed) / 60)}m`;

      if (elapsed >= durationSec) {
        clearInterval(timer);
        timeText.textContent = "완료!";
        timeText.style.fontSize = "14px";
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
