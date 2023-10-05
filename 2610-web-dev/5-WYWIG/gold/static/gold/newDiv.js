// get necessary elements
const lowerDiv = document.getElementById("lowerDiv");

// url
let protocol = window.location.protocol;
let hostname = window.location.hostname;
let port = window.location.port;

// Generate new div
function callback() {
    // create new div
    const newDiv = document.createElement('div');
    // create url
    var value = document.getElementById("unit").value;
    var myArray = value.split("(");
    myArray = myArray[1].split(")");
    unit = myArray[0];
    var weight = document.getElementById("weight").value;
    var url2 = `${protocol}//${hostname}:${port}/unitconv/convert?from=${unit}&to=t_oz&value=${weight}`
    // add timestamp
    const newSpan = document.createElement('span')
    const event = new Date();
    const options = { year: 'numeric', month: 'numeric', day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric'};
    const date = event.toLocaleDateString(undefined, options);
    const dateNode = document.createTextNode(date + " -- ");
    newSpan.appendChild(dateNode);
    newDiv.appendChild(newSpan);
    
    var content;
    // handle errors
    if (weight === "" || unit === "" || weight.isNaN || weight < 0) { // check for all error conditions
        newDiv.style.backgroundColor = "red";
        // find error condition
        if (weight.isNaN) { // validate weight is numeric
            content = document.createTextNode("Error! Weight needs to be a number!");
        } else if (weight < 0) { // validate weight is a positive number
            content = document.createTextNode("Error! Weight needs to be a non-negative number!");
        } else { // didn't select a weight and/or unit
            content = document.createTextNode("Error! Invalid weight or unit!");
        }
        newDiv.appendChild(content);
    } else {
        // use selected color
        newDiv.style.backgroundColor = "gray";
        // compute price - parse unit
        var weigthInTOZ;
        fetch(url2)
            .then( response => response.json())
            .then( json => {
                if (json.error) {
                    content = document.createTextNode("Error! Invalid weight or unit!");
                    newDiv.appendChild(content);
                } else {
                    weigthInTOZ = `${json.value}`;
                    // calculate value
                    value = weigthInTOZ * price;
                    // print result
                    content = document.createTextNode("Your weight of " + weight + " " + unit + " is " + weigthInTOZ + " Troy Ounces, and is worth $" + value + " USD with the current gold price.");
                    newDiv.appendChild(content);
                }
            })
        }
        
    // newDiv.appendChild(content);
    newDiv.style.textAlign = "Center";

    // onclick delete 
    newDiv.onclick = function() { this.remove(); };

    // insert above existing results
    lowerDiv.insertBefore(newDiv, lowerDiv.firstChild);
}
