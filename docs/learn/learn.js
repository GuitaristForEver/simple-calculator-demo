const storageKey = "sc-learning-progress";
const guideInputs = Array.from(document.querySelectorAll("[data-guide]"));
const progressFill = document.querySelector("[data-progress]");
const progressText = document.querySelector("[data-progress-text]");
const resetButton = document.querySelector("[data-reset]");
const copyButton = document.querySelector("[data-copy]");
const copyTarget = document.querySelector("[data-copy-target]");
const copyStatus = document.querySelector("[data-copy-status]");
const focusToggle = document.querySelector("#toggleFocus");

const safeParse = (value) => {
  try {
    return JSON.parse(value);
  } catch (error) {
    return null;
  }
};

const loadProgress = () => {
  const saved = safeParse(localStorage.getItem(storageKey)) || {};
  guideInputs.forEach((input) => {
    input.checked = Boolean(saved[input.dataset.guide]);
  });
  updateProgress();
};

const updateProgress = () => {
  const total = guideInputs.length;
  const done = guideInputs.filter((input) => input.checked).length;
  const percent = total === 0 ? 0 : Math.round((done / total) * 100);

  if (progressFill) {
    progressFill.style.width = `${percent}%`;
  }

  if (progressText) {
    progressText.textContent = `${done}/${total} complete`;
  }

  const payload = {};
  guideInputs.forEach((input) => {
    payload[input.dataset.guide] = input.checked;
  });
  localStorage.setItem(storageKey, JSON.stringify(payload));
};

const resetProgress = () => {
  guideInputs.forEach((input) => {
    input.checked = false;
  });
  updateProgress();
};

const copyCommands = async () => {
  if (!copyTarget) {
    return;
  }

  const text = copyTarget.textContent.trim();
  let success = false;

  if (navigator.clipboard && window.isSecureContext) {
    try {
      await navigator.clipboard.writeText(text);
      success = true;
    } catch (error) {
      success = false;
    }
  }

  if (!success) {
    const helper = document.createElement("textarea");
    helper.value = text;
    helper.setAttribute("readonly", "");
    helper.style.position = "absolute";
    helper.style.left = "-9999px";
    document.body.appendChild(helper);
    helper.select();
    success = document.execCommand("copy");
    document.body.removeChild(helper);
  }

  if (copyStatus) {
    copyStatus.textContent = success ? "Copied." : "Copy failed.";
    setTimeout(() => {
      copyStatus.textContent = "";
    }, 2000);
  }
};

const toggleFocus = () => {
  document.body.classList.toggle("focus");
  if (focusToggle) {
    focusToggle.textContent = document.body.classList.contains("focus")
      ? "Exit Focus"
      : "Focus Mode";
  }
};

const initSlideshow = () => {
  const slideshow = document.querySelector(".slideshow");
  if (!slideshow) {
    return;
  }

  const track = slideshow.querySelector("[data-track]");
  const slides = Array.from(slideshow.querySelectorAll("[data-slide]"));
  const prevButton = slideshow.querySelector("[data-prev]");
  const nextButton = slideshow.querySelector("[data-next]");
  const dotsContainer = slideshow.querySelector("[data-dots]");
  const counter = slideshow.querySelector("[data-counter]");

  if (!track || slides.length === 0) {
    return;
  }

  let index = 0;
  const dots = [];

  const clampIndex = (value) => {
    if (slides.length === 0) {
      return 0;
    }
    return (value + slides.length) % slides.length;
  };

  const updateSlides = () => {
    track.style.transform = `translateX(-${index * 100}%)`;
    if (counter) {
      counter.textContent = `${index + 1} / ${slides.length}`;
    }
    dots.forEach((dot, dotIndex) => {
      dot.classList.toggle("active", dotIndex === index);
    });
  };

  if (dotsContainer) {
    slides.forEach((_, dotIndex) => {
      const dot = document.createElement("button");
      dot.type = "button";
      dot.className = "slide-dot";
      dot.setAttribute("aria-label", `Go to step ${dotIndex + 1}`);
      dot.addEventListener("click", () => {
        index = dotIndex;
        updateSlides();
      });
      dotsContainer.appendChild(dot);
      dots.push(dot);
    });
  }

  if (prevButton) {
    prevButton.addEventListener("click", () => {
      index = clampIndex(index - 1);
      updateSlides();
    });
  }

  if (nextButton) {
    nextButton.addEventListener("click", () => {
      index = clampIndex(index + 1);
      updateSlides();
    });
  }

  updateSlides();
};

guideInputs.forEach((input) => {
  input.addEventListener("change", updateProgress);
});

if (resetButton) {
  resetButton.addEventListener("click", resetProgress);
}

if (copyButton) {
  copyButton.addEventListener("click", copyCommands);
}

if (focusToggle) {
  focusToggle.addEventListener("click", toggleFocus);
}

loadProgress();
initSlideshow();
