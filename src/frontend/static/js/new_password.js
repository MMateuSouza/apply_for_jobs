(function () {
  var allowLetterInput = document.querySelector("#allow_letters");
  var allowUppercaseLettersInput = document.querySelector("#allow_uppercase_letters");
  var allowLowecaseLettersInput = document.querySelector("#allow_lowercase_letters");
  var letterVariation = document.querySelector("#letter_variation");

  document.querySelectorAll('input.form-control').forEach((el) => {
    el.addEventListener('input', (e) => {
      let target = e.target;
      let targetValue = target.value;
      let isInvalid = target.classList.contains('is-invalid');

      !targetValue && !isInvalid && target.classList.add('is-invalid');
      targetValue && isInvalid && target.classList.remove('is-invalid');
    })
  });

  function unckeckLettersVariation() {
    allowLowecaseLettersInput.checked = false;
    allowUppercaseLettersInput.checked = false;
    return true;
  }

  function checkLettersState(el) {
    let allowLetters = el.checked;

    allowLetters && letterVariation.classList.remove("d-none");
    !allowLetters && unckeckLettersVariation() && letterVariation.classList.add("d-none");
  }

  allowLetterInput.addEventListener("input", (el) => {
    checkLettersState(el.target);
  });

  checkLettersState(allowLetterInput);

})();