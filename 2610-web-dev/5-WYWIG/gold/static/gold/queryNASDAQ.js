// store in global variable
var price;

// init message 
const priceMessage = document.getElementById("priceMessage");
priceMessage.innerHTML = "Please Wait...";

// get current date
// TODO: make work over holidays/last available date ---------------------------------------------------------------------------------------------
const event2 = new Date();
const currYear = event2.toLocaleDateString(undefined, { year: 'numeric'});
const currMonth = event2.toLocaleDateString(undefined, { month: 'numeric'});
const currDay = event2.toLocaleDateString(undefined, { day: 'numeric'});

// format current date //2022-11-11
const currDate = currYear + "-" + currMonth + "-" + currDay;

var url = 'https://data.nasdaq.com/api/v3/datasets/LBMA/GOLD?start_date=' + currDate + '&end_date=' + currDate + '&api_key=9LyB2J9n8kZbgof-W3kM';

// get data from nasdaq
fetch(url)
    .then(response => response.json())
    .then(json => {
        // pull out just the USD curr price
        price = json.dataset.data[0][1]
        console.log(`Price = ${price}`);
        priceMessage.innerHTML = "All done!";
    })
    .catch(err => {
        priceMessage.innerHTML = "Error retrieving price of gold! Try again later!";
    })
    .finally(() => {
        // document.querySelector('#message').innerHTML = "All done!";
    });
