(function () {
  var allowLetterInput = document.querySelector("#allow_letters");
  var allowUppercaseLettersInput = document.querySelector("#allow_uppercase_letters");
  var allowLowecaseLettersInput = document.querySelector("#allow_lowercase_letters");
  var letterVariation = document.querySelector("#letter_variation");

  function unckeckLettersVariation() {
    allowLowecaseLettersInput.checked = false;
    allowUppercaseLettersInput.checked = false;
    return true;
  }

  allowLetterInput.addEventListener("input", (el) => {
    let allowLetters = el.target.checked;

    allowLetters && letterVariation.classList.remove("d-none");
    !allowLetters && unckeckLettersVariation() && letterVariation.classList.add("d-none");
  });
})();