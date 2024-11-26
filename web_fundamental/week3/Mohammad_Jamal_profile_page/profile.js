function user() {
  // Select the <h3> element by its id
    var newname = document.querySelector("#username");

  // Update the text content to "Jamal"
    newname.innerText = "Jamal Mohammad";
}



function removeRequest(request1, status, request2) {
  // Get the specific connection request element
  const requestElement = document.getElementById(request1, request2);

 if (requestElement) {
    // Update the request element based on the status
    if (status === "accepted") {
      requestElement.innerText = " ";
    } else if (status === "declined") {
      requestElement.innerText = " ";
    }
  }
}


