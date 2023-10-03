// script.js
function myfunc(a, b) {
    let x = a;
    let y = b;
    return {
        sum: x + y,
        product: x * y,
        difference: x - y,
        division: x / y,
        remainder: x % y,
        increment: x++,
        decrement: x--,
        square: x ** 2
    };
}

document.getElementById("calculatorForm").addEventListener("submit", function (event) {
    event.preventDefault();
    const inputA = parseFloat(document.getElementById("inputA").value);
    const inputB = parseFloat(document.getElementById("inputB").value);

    const result = myfunc(inputA, inputB);

    const resultsContainer = document.getElementById("results");
    resultsContainer.innerHTML = `
        <p>Sum: ${result.sum}</p>
        <p>Product: ${result.product}</p>
        <p>Difference: ${result.difference}</p>
        <p>Division: ${result.division}</p>
        <p>Remainder: ${result.remainder}</p>
        <p>Increment: ${result.increment}</p>
        <p>Decrement: ${result.decrement}</p>
        <p>Square: ${result.square}</p>
    `;
});
