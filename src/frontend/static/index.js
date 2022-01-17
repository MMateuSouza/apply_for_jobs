(function () {
  var copyToClipboardButtons = document.querySelectorAll("button.copy-to-clipboard");

  copyToClipboardButtons.forEach((el) => {
    el.addEventListener("click", (event) => {
      let parentNode = event.target.parentNode;
      let passwordLinkInput = parentNode.querySelector("input");
      let passwordLink = passwordLinkInput.value || null;

      if (!passwordLink) {
        alert("Erro ao copiar o link para senha!");
        return;
      }

      navigator.clipboard.writeText(passwordLink);
      alert("Link copiado!");
    });
  });
})();