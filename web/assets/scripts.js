const object = document.querySelector('.object');

function moveObject() {
    const newX = Math.random() * (window.innerWidth - 50);
    const newY = Math.random() * (window.innerHeight - 50);

    object.style.left = `${newX}px`;
    object.style.top = `${newY}px`;
}

setInterval(moveObject, 2000); // Move the object every 2 seconds
