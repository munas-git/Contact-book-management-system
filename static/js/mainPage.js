// var modal = Array.from(document.getElementsByClassName("contact_modal"));
// var manageProfileBtn = Array.from(document.getElementsByClassName("modal_btn"));
// var span = Array.from(document.getElementsByClassName("close"));

// for (let i = 0; i < modal.length; i++) {
//   // btn[i].onclick = function () {
//   //   modal[i].style.display = "block";
//   //   document.body.style.overflow = "hidden";
//   // // };
//   // span[i].onclick = function () {
//   //   modal[i].style.display = "none";
//   //   document.body.style.overflow = "auto";
//   };

var btn = document.querySelectorAll(".modal_btn");

// All page modals
var modals = document.querySelectorAll(".modal");

// Get the <span> element that closes the modal
var spans = document.getElementsByClassName("close");

// When the user clicks the button, open the modal
for (var i = 0; i < btn.length; i++) {
  btn[i].onclick = function (e) {
    e.preventDefault();
    document.body.style.overflow = "hidden";
    modal = document.querySelector(e.target.getAttribute("href"));
    modal.style.display = "block";
  };
}

// When the user clicks on <span> (x), close the modal
for (var i = 0; i < spans.length; i++) {
  spans[i].onclick = function () {
    for (var index in modals) {
      if (typeof modals[index].style !== "undefined")
        modals[index].style.display = "none";
      document.body.style.overflow = "auto";
    }
  };
}
//Manage Profile Modal
// var manageProfileBtn = document.getElementById("manage_profile");
// var manageProfileModal = document.getElementById("user_manage_profile");
// var manageProfileSpan = document.getElementById("close_manage_profile");

// manageProfileBtn.onclick = function () {
//   manageProfileModal.style.display = "block";
//   document.body.style.overflow = "hidden";
// };
// manageProfileSpan.onclick = function () {
//   manageProfileModal.style.display = "none";
//   document.body.style.overflow = "auto";
// };

// var editContactBtn = document.getElementById("edit_contact");
// var editContactModal = document.getElementById("user_edit_contact");
// var editContactSpan = document.getElementById("close_edit_contact");

// editContactBtn.onclick = function () {
//   editContactModal.style.display = "block";
//   document.body.style.overflow = "hidden";
// };
// editContactSpan.onclick = function () {
//   editContactModal.style.display = "none";
//   document.body.style.overflow = "auto";
// };

function changeIcon(anchor) {
  var icon = anchor.querySelector("i");
  icon.classList.toggle("fa-regular");
  icon.classList.toggle("fa-solid");

  icon.classList.contains("fa-regular") ? (isFave = true) : (isFave = false);
}

function deleteContact() {}

function searchContact() {
  let input = document.getElementById("searchbar").value;
  input = input.toLowerCase();
  let searchList = document.getElementsByClassName("contact");

  for (i = 0; i < searchList.length; i++) {
    if (!searchList[i].innerHTML.toLowerCase().includes(input)) {
      searchList[i].style.display = "none";
    } else {
      searchList[i].style.display = "flex";
    }
  }
}
//For add contact
var loadNewFile = function (event) {
  var newContactImg = document.getElementById("add_new_contact");
  var url = URL.createObjectURL(event.target.files[0]);
  newContactImg.style.backgroundImage = "url(" + url + ")";
  console.log(URL.createObjectURL(event.target.files[0]));
  alert(event.target.files[0].name);
  var upload_icon = document.getElementById("upload_icon");
  upload_icon.style.display = "none";
};
//For edit contact
var loadFile = function (event) {
  var editContactImg = document.getElementById("edit_contact_img");
  var url = URL.createObjectURL(event.target.files[1]);
  editContactImg.style.backgroundImage = "url(" + url + ")";
  console.log(URL.createObjectURL(event.target.files[0]));
  console.log("first");
  console.log(URL.createObjectURL(event.target.files[1]));
  alert(event.target.files[0].name);
};

// var imgBox = Array.from(document.getElementsByClassName("imgBox"));
// var upload_icon = Array.from(document.getElementsByClassName("upload_icon"));

// for (let i = 0; i < imgBox.length; i++) {
//   var loadFile = function (event) {
//     var url = URL.createObjectURL(event.target.files[0]);
//     imgBox[i].style.backgroundImage = "url(" + url + ")";
//     console.log(URL.createObjectURL(event.target.files[0]));
//     alert(event.target.files[0].name);
//     upload_icon[i].style.display = "none";
//     console.log("first");
//   };
// }

// const checkbox = document.getElementById("checkbox");
// const header = document.getElementsByClassName("header")[0];
// const icons = document.getElementsByClassName("nav_icons")[0];

// checkbox.addEventListener("change", () => {
//   document.body.classList.toggle("darkmode");

//   // header.style.backgroundColor = "#000";
//   var mn = getElementsByClassName("contact_modal")[0];
//   mn.classList.toggle("darkmode");

//   // icons.style.color = "#fffff";
// });
function toggleEnable(id) {
  var textbox = document.getElementById(id);
  console.log("first");
  if (textbox.disabled) {
    // If disabled, do this
    document.getElementById(id).disabled = false;
  } else {
    // Enter code here
    document.getElementById(id).disabled = true;
  }
}
// function toggleEnable1(id) {
//   var textbox = document.getElementById(id);
//   console.log("first");
//   if (textbox.disabled) {
//     // If disabled, do this
//     document.getElementById(id).disabled = false;
//   } else {
//     // Enter code here
//     document.getElementById(id).disabled = true;
//   }
// }

// function addContact() {
//   //values
//   var name = document.getElementById("fullname").value;
//   var role = document.getElementById("role").value;
//   var phoneNumber = document.getElementById("number").value;
//   var email = document.getElementById("email").value;

//   //
//   var contactlist = document.querySelector(".contactlist");

//   //new divs
//   var contact = document.createElement("div");
//   var mainContact = document.createElement("div");
//   var manageContact = document.createElement("div");
//   var contactName = document.createElement("div");
//   var contactOtherDetails = document.createElement("div");
//   var nameAndRole = document.createElement("div");

//   var favourite = document.createElement("span");
//   var edit = document.createElement("span");
//   var deleteBtn = document.createElement("span");

//   var nameH5 = document.createElement("H5");
//   var emailH5 = document.createElement("H5");
//   var numberH5 = document.createElement("H5");
//   var roleP = document.createElement("p");

//   contact.className = "contact";
//   mainContact.className = "main_contact";
//   manageContact.className = "manage_contact";
//   contactName.className = "contact_name";
//   contactOtherDetails.className = "contact_other_details";
//   nameAndRole.className = "name_and_role";

//   contactlist.appendChild(contact);
//   contact.appendChild(mainContact);
//   contact.appendChild(manageContact);

//   mainContact.appendChild(contactName);
//   mainContact.appendChild(contactOtherDetails);
//   contactName.appendChild(nameAndRole);
//   nameAndRole.appendChild(nameH5);
//   nameAndRole.appendChild(roleP);
//   contactOtherDetails.appendChild(numberH5);
//   contactOtherDetails.appendChild(emailH5);

//   manageContact.appendChild(favourite);
//   manageContact.appendChild(edit);
//   manageContact.appendChild(deleteBtn);

//   //   var p = document.getElementsByClassName("contact")[0];
//   //   p.classList.add("lol");

//   nameH5.innerHTML = '<i class="fa-solid fa-user"></i>' + " " + name;
//   roleP.innerHTML = role;
//   emailH5.innerHTML = '<i class="fa-solid fa-envelope"></i>' + " " + email;
//   numberH5.innerHTML = '<i class="fa-solid fa-phone"></i>' + " " + phoneNumber;

//   favourite.innerHTML = '<i class="fa-regular fa-star"></i>';
//   edit.innerHTML = '<i class="fa-solid fa-pen-to-square"></i>';
//   deleteBtn.innerHTML = '<i class="fa-solid fa-trash"></i>';

//   //contact.setAttribute("class", "red");
// }
