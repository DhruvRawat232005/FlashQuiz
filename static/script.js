document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector(".quiz-form");
  const submitBtn = document.querySelector(".submit-btn");

  // Scroll to next question on selection (optional UX)
  const radios = document.querySelectorAll("input[type='radio']");
  radios.forEach((radio) => {
    radio.addEventListener("change", (e) => {
      const currentCard = e.target.closest(".question-card");
      const nextCard = currentCard.nextElementSibling;
      if (nextCard && nextCard.classList.contains("question-card")) {
        nextCard.scrollIntoView({ behavior: "smooth" });
      }
    });
  });

  // Prevent double submit
  if (form && submitBtn) {
    form.addEventListener("submit", () => {
      submitBtn.disabled = true;
      submitBtn.innerText = "Submitting...";
    });
  }

  // Optional: highlight selected option (basic)
  const allLabels = document.querySelectorAll(".options label");
  allLabels.forEach(label => {
    label.addEventListener("click", () => {
      const parent = label.closest(".options");
      parent.querySelectorAll("label").forEach(l => l.classList.remove("selected"));
      label.classList.add("selected");
    });
  });
});
