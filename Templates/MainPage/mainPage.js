var modal = document.getElementsByClassName("contact_modal")[0];
var btn = document.getElementsByClassName("modal_btn")[0];
var span = document.getElementsByClassName("close")[0];

var editModal = document.getElementsByClassName("contact_modal")[1];
var editBtn = document.getElementsByClassName("modal_btn")[1];
var editSpan = document.getElementsByClassName("close")[1];

var isFave;
// var edit_modal = document.getElementsByClassName("add_contact_modal")[0];
// var edit_btn = document.getElementsByClassName("modal_btn")[0];
// var editspan = document.getElementsByClassName("close")[0];

btn.onclick = function () {
  modal.style.display = "block";
  document.body.style.overflow = "hidden";
};
span.onclick = function () {
  modal.style.display = "none";
  document.body.style.overflow = "auto";
};

editBtn.onclick = function () {
  editModal.style.display = "block";
  document.body.style.overflow = "hidden";
};
editSpan.onclick = function () {
  editModal.style.display = "none";
  document.body.style.overflow = "auto";
};

function changeIcon(anchor) {
  var icon = anchor.querySelector("i");
  icon.classList.toggle("fa-regular");
  icon.classList.toggle("fa-solid");

  icon.classList.contains("fa-regular") ? (isFave = true) : (isFave = false);
}

function deleteContact() {
  getElementsByClassName;
}

function addToFave() {
  var fave = document.querySelector("i");
  fave.classList.remove("fa-regular");
  fave.classList.add("fa-solid");
  console.log("pop");
}
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
function addContact() {
  //values
  var name = document.getElementById("fullname").value;
  var role = document.getElementById("role").value;
  var phoneNumber = document.getElementById("number").value;
  var email = document.getElementById("email").value;

  //
  var contactlist = document.querySelector(".contactlist");

  //new divs
  var contact = document.createElement("div");
  var mainContact = document.createElement("div");
  var manageContact = document.createElement("div");
  var contactName = document.createElement("div");
  var contactOtherDetails = document.createElement("div");
  var nameAndRole = document.createElement("div");

  var favourite = document.createElement("span");
  var edit = document.createElement("span");
  var deleteBtn = document.createElement("span");

  var nameH5 = document.createElement("H5");
  var emailH5 = document.createElement("H5");
  var numberH5 = document.createElement("H5");
  var roleP = document.createElement("p");

  contact.className = "contact";
  mainContact.className = "main_contact";
  manageContact.className = "manage_contact";
  contactName.className = "contact_name";
  contactOtherDetails.className = "contact_other_details";
  nameAndRole.className = "name_and_role";

  contactlist.appendChild(contact);
  contact.appendChild(mainContact);
  contact.appendChild(manageContact);

  mainContact.appendChild(contactName);
  mainContact.appendChild(contactOtherDetails);
  contactName.appendChild(nameAndRole);
  nameAndRole.appendChild(nameH5);
  nameAndRole.appendChild(roleP);
  contactOtherDetails.appendChild(numberH5);
  contactOtherDetails.appendChild(emailH5);

  manageContact.appendChild(favourite);
  manageContact.appendChild(edit);
  manageContact.appendChild(deleteBtn);

  //   var p = document.getElementsByClassName("contact")[0];
  //   p.classList.add("lol");

  nameH5.innerHTML = '<i class="fa-solid fa-user"></i>' + " " + name;
  roleP.innerHTML = role;
  emailH5.innerHTML = '<i class="fa-solid fa-envelope"></i>' + " " + email;
  numberH5.innerHTML = '<i class="fa-solid fa-phone"></i>' + " " + phoneNumber;

  favourite.innerHTML = '<i class="fa-regular fa-star"></i>';
  edit.innerHTML = '<i class="fa-solid fa-pen-to-square"></i>';
  deleteBtn.innerHTML = '<i class="fa-solid fa-trash"></i>';

  //contact.setAttribute("class", "red");
}
