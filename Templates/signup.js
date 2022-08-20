// const form = document.getElementById("form");
// const username = document.getElementById("username");
// const email = document.getElementById("email");
// const password = document.getElementById("password");

// // console.log(username.value);

// form.addEventListener("submit", (e) => {
//   e.preventDefaults();

//   checkInputs();
// });

// const checkInputs = () => {
//   const usernameVal = username.value.trim();
//   const emailVal = email.value.trim();
//   const passwordVal = password.value.trim();

//   if (usernameVal === " ") {
//     errorMessage(username, "Username cannot be blank");
//   } else {
//     successMessage(username);
//   }
// };

// const errorMessage = (input, message) => {
//   const formControl = input.parentElement;
//   const small = formControl.querySelector("small");

//   small.innerText = message;
//   formControl.className = "input-field";
// };
