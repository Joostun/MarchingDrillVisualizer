const input = document.querySelector("input");
const preview = document.querySelector(".preview");

input.style.opacity = 0;

function fetchFromAPI() {
    const curFiles = input.files;
    if (curFiles.length === 0) {
      const para = document.createElement("p");
      para.textContent = "No files currently selected for upload";
      preview.appendChild(para);
    } else {
      fetch('http://127.0.0.1:5000/api/retrieveMarcher',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(curFiles[0])
        })
        .then(response => document.write(response.status))
      }
    }
    

  
input.addEventListener("change", fetchFromAPI);
