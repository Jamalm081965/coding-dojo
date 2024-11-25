// Change Login to Logout
const loginBtn = document.getElementById("login-btn");
loginBtn.addEventListener("click", () => {
  if (loginBtn.textContent === "Login") {
    loginBtn.textContent = "Logout";
  } else {
    loginBtn.textContent = "Login";
  }
});

// Remove Add Definition button on click
const addDefinitionBtn = document.getElementById("add-definition-btn");
addDefinitionBtn.addEventListener("click", () => {
  addDefinitionBtn.remove();
});

// Add alert when Like button is clicked
const likeButtons = document.querySelectorAll(".like-btn");
likeButtons.forEach((button) => {
  button.addEventListener("click", () => {
    alert("Ninja was liked");
  });
});
