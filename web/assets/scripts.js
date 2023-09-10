const fileInput = document.getElementById("fileInput");
const uploadButton = document.getElementById("uploadButton");
const statusMessage = document.getElementById("statusMessage");
// Add an event listener to handle the file upload when the button is clicked
uploadButton.addEventListener("click", () => {
    const selectedFile = fileInput.files[0];
    if (selectedFile) {
        // Create a FormData object to send the file
        const formData = new FormData();
        formData.append("pdfFile", selectedFile, selectedFile.name);

        // Make a POST request to your Flask server
        fetch("http://localhost:5000/api/retrieveMarcher", {
            method: "POST",
            body: formData,
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // Display a success message or handle the response data as needed
            statusMessage.textContent = "PDF uploaded successfully!";
        })
        .catch(error => {
            // Handle any errors that occurred during the fetch
            statusMessage.textContent = `Error: ${error.message}`;
        });
    }
});