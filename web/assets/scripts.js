let marcher_list = [];
let setNumber = 0;
let start, previousTimeStamp;
const c = document.getElementById("canvas");
var ctx = c.getContext("2d")
let set = 0;

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
      console.log(marcher_list);  
  })
});

//adjust Coordinates to match the canvas dimensions
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

let xDiff = [];
let yDiff = [];
for(item in marcher_list){
  let counts = item.counts
  for(let stepIndex = 0; stepIndex < ( item.counts.length-1); stepIndex++){
    let xSubDiff = [];
    let ySubDiff = [];
    //x step size
    xSubDiff.push(item.x[set+1] - item.x[set]);
    //y step size
    ySubDiff.push(item.y[set+1] - item.y[set]);

    //Add to xDiff and yDiff
    xDiff.push(xSubDiff);
    yDiff.push(ysubDiff);
  }
}
  
function setMarcher(startTime){
  let setTime = marcher_list[0].counts[set] * 500;
  if(setTime == 0){
    setTime = 4000;
  }
  let currentTime = new Date.now();
  let elapsedTime = currentTime - startTime;
  console.log(elapsedTime);
  console.log(startTime);
  let timeFrac = elapsedTime / setTime;
  console.log(timeFrac)
  if(elapsedTime > setTime){
    timeFrac = 1;
  }
  ctx.clearRect(0, 0, 1080, 480); // clear canvas
  for(let marcherListIndex = 0; marcherListIndex < marcher_list.length; marcherListIndex++) {
      let item = marcher_list[marcherListIndex]
      ctx.beginPath();
      let xStepped = xDiff[marcherListIndex][set] * timeFrac;
      let yStepped = yDiff[marcherListIndex][set] * timeFrac;
      ctx.arc(item.x[set] + xStepped, item.y[set] + yStepped, 5, 2*Math.PI, false);
      ctx.fillstyle = "blue";
      ctx.fill();
      ctx.closePath();
  }
}

function myRepeatFunction(event) {
  this.innerHTML = "Elapsed time: " + event.elapsedTime;
}

document.getElementById("initializeMarching").addEventListener("click", () => {
  const startTime = new Date();
  console.log(startTime);
  console.log(event.elapsedTime);
  window.requestAnimationFrame(setMarcher(startTime));
  set++ 
});