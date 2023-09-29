let marcher_list = [];
let setNumber = 0;
let start, previousTimeStamp;
const c = document.getElementById("canvas");
var ctx = c.getContext("2d");
const undo = document.getElementById("undoMarching");
const fwds = document.getElementById("initializeMarching");
let set = 0;
let xDiff = [];
let yDiff = [];

//hiding buttons functions
function hideButtons() {
  undo.hidden = true;
  fwds.hidden = true;
}

function unhideButtons(){
  undo.hidden = false;
  fwds.hidden = false;
}

//hide buttons on start
hideButtons();

//pdf upload code
document.getElementById("uploadButton").addEventListener("click", () => {
  const pdfInput = document.getElementById("pdfInput");
  const statusMessage = document.getElementById("statusMessage");

  const pdfFile = pdfInput.files[0];

  if (!pdfFile) {
      statusMessage.textContent = "No file selected.";
      return;
  }

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
      stepCalc();
      unhideButtons();
      statusMessage.textContent = "Ready to Run!";
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

//calculated step sizes
function stepCalc(){
  xDiff = [];
  yDiff = [];
  for(let i = 0; i < marcher_list.length; i++){
    item = marcher_list[i];
    let counts = item.counts;
    let xSubDiff = [];
    let ySubDiff = [];
    for(let stepIndex = 0; stepIndex < (counts.length-1); stepIndex++){
      //x step size
      xSubDiff.push(item.x[stepIndex+1] - item.x[stepIndex]);
      //y step size
      ySubDiff.push(item.y[stepIndex+1] - item.y[stepIndex]);
      //Add to xDiff and yDiff
    }
    xDiff.push(xSubDiff);
    yDiff.push(ySubDiff);
  }
}  

function setForwardsMarcher(startTime){
  let setTime = marcher_list[0].counts[set] * 200;
  if(setTime == 0){
    setTime = 2000;
  }
  let currentTime = Date.now();
  let elapsedTime = currentTime - startTime;
  let timeFrac = elapsedTime / setTime;
  if(elapsedTime > setTime){  
    timeFrac = 1;
  } 
  ctx.clearRect(0, 0, 1080, 480);
  console.log(set)
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
  if(timeFrac >= 1){
    clearInterval(marchInterval);
    unhideButtons();
    console.log("its done ");
  } 
}

function setBackwardsMarcher(startTime){
  let setTime = marcher_list[0].counts[set] * 200;
  if(setTime == 0){
    setTime = 2000;
  }
  let currentTime = Date.now();
  let elapsedTime = currentTime - startTime;
  let timeFrac = elapsedTime / setTime;
  if(elapsedTime > setTime){  
    timeFrac = 1;
  } 
  ctx.clearRect(0, 0, 1080, 480);
  for(let marcherListIndex = 0; marcherListIndex < marcher_list.length; marcherListIndex++) {
      let item = marcher_list[marcherListIndex]
      ctx.beginPath();
      let xStepped = xDiff[marcherListIndex][set+1] * timeFrac;
      let yStepped = yDiff[marcherListIndex][set+1] * timeFrac;
      ctx.arc(item.x[set+2] - xStepped, item.y[set+2] - yStepped, 5, 2*Math.PI, false);
      ctx.fillstyle = "blue";
      ctx.fill();
      ctx.closePath();
  }
  if(timeFrac >= 1){
    clearInterval(marchInterval);
    console.log("its done ");
    unhideButtons();
  } 
}

function myRepeatFunction(event) {
  this.innerHTML = "Elapsed time: " + event.elapsedTime;
}

document.getElementById("initializeMarching").addEventListener("click", () => {
  hideButtons()
  const startTime = Date.now();
  console.log(startTime);
  marchInterval = setInterval(() => setForwardsMarcher(startTime), 10);
  set++;
});

document.getElementById("undoMarching").addEventListener("click", () => {
  hideButtons()
  const startTime = Date.now();
  console.log(startTime);
  marchInterval = setInterval(() => setBackwardsMarcher(startTime), 10);
  set--;
}); 