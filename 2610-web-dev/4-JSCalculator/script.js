// replace title
document.title = "JS Calculator";

// Make div for calculator ---------------------------------------------------------------------------------------------
const main = document.createElement('div');
main.style.backgroundColor = "gray";

// title text
const p1 = document.createElement('p');
const mainText = document.createTextNode("JS Calculator");
p1.style.textAlign = "Center";
p1.appendChild(mainText);
main.appendChild(p1);

// descriptive text
const p2 = document.createElement('p');
const descriptionText = document.createTextNode("Create an Expression");
p2.style.textAlign = "Center";
p2.appendChild(descriptionText);
main.appendChild(p2);

// operandOne  ---------------------------------------------------------------------------------------------
const p3 = document.createElement('p');
const operandOne = document.createElement('input');
operandOne.id = "operandOne";
operandOne.setAttribute('type', 'number');
operandOne.setAttribute('value', '12');
p3.appendChild(operandOne);


// operator ---------------------------------------------------------------------------------------------
const op = document.createElement("select");
op.id = "operator";
const options = ["+", "-", "/", "*", "%", "**"];
// input children
for (var i = 0; i < options.length; i++) {
    var option = document.createElement("option");
    option.innerHTML = options[i];
    op.appendChild(option);
}
p3.appendChild(op);

// second operand ---------------------------------------------------------------------------------------------
const operandTwo = document.createElement('input');
operandTwo.id = "operandTwo";
operandTwo.setAttribute('type', 'number');
operandTwo.setAttribute('value', '4');
p3.appendChild(operandTwo);

// input for color ---------------------------------------------------------------------------------------------
const p4 = document.createElement('p')
const colorInput = document.createElement('input');
colorInput.id = "colorInput"
colorInput.setAttribute('type', 'color');
p4.appendChild(colorInput);
const colorText = document.createTextNode("Color Of New Result <Div>");
p4.appendChild(colorText);
p4.style.textAlign = "center";

// create space for computational divs -----------------------------------------------------------------------
const lowerDiv = document.createElement('div');

// enter button ---------------------------------------------------------------------------------------------
const enter = document.createElement('button');
enter.innerHTML = "Compute";
enter.onclick = function() {result(operandOne.value, operandTwo.value, op.value, colorInput.value)};
p3.appendChild(enter);
p3.style.textAlign = "center";
main.appendChild(p3);
main.appendChild(p4); // add colorInput to main

// add main/lowerDiv to document
document.body.appendChild(main);
document.body.appendChild(lowerDiv);


// generate new div ---------------------------------------------------------------------------------------------
function result(operandOne, operandTwo, op, color) {
    const newDiv = document.createElement('div');
    // add timestamp
    const newSpan = document.createElement('span')
    const event = new Date();
    const options = { year: 'numeric', month: 'numeric', day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric'};
    const date = event.toLocaleDateString(undefined, options);
    const dateNode = document.createTextNode(date + " -- ");
    newSpan.appendChild(dateNode);
    newDiv.appendChild(newSpan);
    
    var content;
    // handle error
    if (operandOne === "" || operandTwo === "") {
        newDiv.style.backgroundColor = "red";
        content = document.createTextNode("Error! Missing Operand!");
    } else {
        // use selected color
        newDiv.style.backgroundColor = color;
        // compute result - parse operator
        var result;
        switch (op) {
            case '+': result = parseFloat(operandOne) + parseFloat(operandTwo); break;
            case '-': result = parseFloat(operandOne) - parseFloat(operandTwo); break;
            case '/': result = parseFloat(operandOne) / parseFloat(operandTwo); break;
            case '*': result = parseFloat(operandOne) * parseFloat(operandTwo); break;
            case '%': result = parseFloat(operandOne) % parseFloat(operandTwo); break;
            case '**': result = parseFloat(operandOne) ** parseFloat(operandTwo); break;
        }
        // print result
        content = document.createTextNode(operandOne + " " + op + " " + operandTwo + " = " + result);
    }
    newDiv.appendChild(content);
    newDiv.style.textAlign = "Center";

    // onclick delete 
    newDiv.onclick = function() {this.remove();};

    // insert above existing results
    lowerDiv.insertBefore(newDiv, lowerDiv.firstChild);
}
