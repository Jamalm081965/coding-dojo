
//define the function to hover //
function addSucculentPic2(element) {
  var pic2 = document.getElementById("SucculentPic2");
  var pic1 = element;
  pic1.style.display = "none"; // Hide the first image
  pic2.style.display = "block"; // Show the second image
}

function removeSucculentPic2(element) {
  var pic2 = document.getElementById("SucculentPic2");
  var pic1 = element;
  pic1.style.display = "block"; // Show the first image
  pic2.style.display = "none"; // Hide the second image
}
// Function to show the caution box
function showCautionBox() {
    document.getElementById('cautionBox').style.display = 'block';
}

// Function to close the caution box
function closeCautionBox() {
    document.getElementById('cautionBox').style.display = 'none';
}

// Automatically show the caution box when the page loads
window.onload = function () {
    showCautionBox();
};