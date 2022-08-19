function changeIcon(anchor) {
  var icon = anchor.querySelector("i");
  icon.classList.toggle("fa-regular");
  icon.classList.toggle("fa-solid");

  anchor.querySelector("span").textContent = icon.classList.contains(
    "fa-regular"
  )
    ? "Read more"
    : "Read less";
}
