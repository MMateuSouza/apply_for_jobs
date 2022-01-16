(function () {
  var modalPasswordVisualization = document.querySelector("#modal-password-visualization");
  var loader = document.querySelector("#loader");

  function showOrHideLoader() {
    let isLoaderDisabled = loader.classList.contains("d-none");

    isLoaderDisabled && loader.classList.remove("d-none");
    !isLoaderDisabled && loader.classList.add("d-none");
  }

  function generatePasswordSharedLink() {
    console.log("Generate Password Shared Link")
  }

  function visualizePassword() {
    console.log("Password Visualization")
  }

  modalPasswordVisualization.addEventListener("hidden.bs.modal", () => showOrHideLoader());
})();