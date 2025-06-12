// public/loader.js

window.addEventListener("load", function () {
  const observer = new MutationObserver(() => {
    const messages = document.querySelectorAll(".message");

    messages.forEach((msg) => {
      if (msg.innerText.includes("⏳ Processing your task")) {
        if (!msg.querySelector(".loader")) {
          const loader = document.createElement("div");
          loader.className = "loader";
          msg.appendChild(loader);
        }
      }
    });
  });

  observer.observe(document.body, {
    childList: true,
    subtree: true,
  });
});
