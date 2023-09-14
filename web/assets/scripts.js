let marcher_list = []
let setNumber = 0
const dot = new Image()
dot.src = "dot.png"

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
  }).then(data => {
      marcher_list = data
      adjustCoordinates();
      console.log(marcher_list)
      console.log(data)});
      
  })

function adjustCoordinates(){
  for(let marcherIndex = 0; marcherIndex<marcher_list.length; marcherIndex++){
    for(let xcoordinateIndex = 0; xcoordinateIndex < marcher_list[marcherIndex].x.length; xcoordinateIndex++){
      let xtransferCoordinateValue = marcher_list[marcherIndex].x[xcoordinateIndex];
      xtransferCoordinateValue = xtransferCoordinateValue * 9 + 540;
      marcher_list[marcherIndex].x[xcoordinateIndex] = xtransferCoordinateValue;
    }
    for(let ycoordinateIndex = 0; ycoordinateIndex < marcher_list[marcherIndex].y.length; ycoordinateIndex++){
      let ytransferCoordinateValue = marcher_list[marcherIndex].y[ycoordinateIndex];
      ytransferCoordinateValue = 480 - ytransferCoordinateValue * 9;
      marcher_list[marcherIndex].y[ycoordinateIndex] = ytransferCoordinateValue;
    }
  }
}
function setMarcher(){
  ctx.clearRect(0, 0, 1080, 480); // clear canvas
  for(let item of marcher_list) {
    ctx.beginPath();
    ctx.lineTo(item.x[set+1],item.y[set+1]);
    ctx.arc()
    ctx.drawImage(dot, item.x[set], item.y[set]);
    ctx.closePath();
    console.log("it goes!!!")
  }


}

function march(set){
  const c = document.getElementById("canvas");
  var ctx = c.getContext("2d")
  let xDiff = item.x[set+1] - item.x[set]
  let yDiff = item.y[set+1] - item.y[set]
  let counts = item.counts[set]
  let xStepSize = xDiff/counts
  let yStepSize = yDiff/counts
    requestAnimationFrame(animate);
    let xDiff = item.x[set+1] - item.x[set]
    let yDiff = item.y[set+1] - item.y[set]
    let counts = item.counts[set]
    ctx.beginPath();
    ctx.lineTo(item.x[set+1],item.y[set+1]);
    ctx.arc()
    ctx.drawImage(dot, item.x[set], item.y[set]);
    ctx.closePath();
    console.log("it goes!!!")
  }
  setNumber++
}

document.getElementById("initializeMarching").addEventListener("click", () => {
  setInterval(march(setNumber),5000);
});