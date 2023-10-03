document.getElementById("ageForm").addEventListener("submit", function (event) {
    event.preventDefault();

    const age = parseInt(document.getElementById("ageInput").value);

    if (isNaN(age)) {
        document.getElementById("result").innerHTML = "<p>Please enter a valid age.</p>";
    } else {
        if (age >= 18) {
            document.getElementById("result").innerHTML = "<p>You are eligible to access the content. Enjoy!</p>";
        } else {
            document.getElementById("result").innerHTML = "<p>You are not eligible to access the content.</p>";
        }
    }
});
