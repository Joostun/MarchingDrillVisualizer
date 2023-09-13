const marcher_list = [];

document.getElementById("uploadButton").addEventListener("click", () => {
  const pdfInput = document.getElementById("pdfInput");
  const statusMessage = document.getElementById("statusMessage");

  // Get the selected PDF file
  const pdfFile = pdfInput.files[0];

  if (!pdfFile) {
      statusMessage.textContent = "No file selected.";
      return;
  }

  // Create a FormData object to send the file
  const formData = new FormData();
  formData.append("pdfFile", pdfFile);

  // Send a POST request to your Flask server
  fetch("http://127.0.0.1:5000/api/retrieveMarcher", {
      method: "POST",
      body: formData,
  })
  .then(response => {
      return response.json();
  }).then((data) => console.log(data))
    for(let x in data){
      marcher = JSON.parse(x)
      marcher_list.append(marcher)
    };
  });


  