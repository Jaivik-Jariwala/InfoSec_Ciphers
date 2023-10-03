// Countdown using a for loop
const countdownFor = document.getElementById("countdownFor");
for (let i = 99; i >= 0; i--) {
    countdownFor.innerHTML += i + " ";
}

// Countdown using a while loop
const countdownWhile = document.getElementById("countdownWhile");
let j = 100;
while (j >= 0) {
    countdownWhile.innerHTML += j + " ";
    j--;
}
