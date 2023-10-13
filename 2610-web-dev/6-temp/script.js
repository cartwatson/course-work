const vm = Vue.createApp({
    data() {
        return {
            // data
            // -- conditions
            locationLoaded: 0,
            weatherLoaded: 0,
            forecastLoaded: 0,
            // -- location data
            city: "",
            region: "",
            country: "",
            latitude: 0,
            longitude: 0,
            // -- weather data
            date: "",
            temperature: 0,
            tempHigh: 0,
            tempLow: 0,
            conditions: "",
            humidity: 0,
            pressure: 0,
            // forecasts
            unlikelyCounter: 0,
            neutralCounter: 40,
            likelyCounter: 0,
            forecasts: [],
        }
    },
    methods: {
        ForecastAPICall: function() {
            console.log("Forecast API Call starting...")
            fetch("https://api.openweathermap.org/data/2.5/forecast?lat=" + this.latitude + "&lon=" + this.longitude + "&appid=b0ae2ff72b20a14f8fbda94e4e0f0868&units=imperial")
            .then(response => response.json())
            .then(json => {
                console.log(json);
                for (const element of json.list) {
                    // update all other variables
                    var dict = {
                        date: element.dt_txt,
                        temperature: element.main.temp,
                        tempHigh: element.main.temp_max, 
                        tempLow: element.main.temp_min,
                        humidity: element.main.humidity,
                        pressure: element.main.pressure,
                        conditions: element.weather[0].main,
                    }
                    this.forecasts.push(dict);
                }
                this.forecastLoaded = 1;
                console.log("No errors calling forecast API")
            })
            .catch(err => {
                this.forecastLoaded = -1;
                console.log("Error calling forecast API")
            })
        },
        CurrentConditionsAPICall: function() {
            console.log("Weather API Call starting...")
            fetch("https://api.openweathermap.org/data/2.5/weather?lat=" + this.latitude + "&lon=" + this.longitude + "&appid=b0ae2ff72b20a14f8fbda94e4e0f0868&units=imperial")
            .then(response => response.json())
            .then(json => {
                console.log(json);
                // get dates
                var date = new Date(json.dt*1000);
                var year = date.getFullYear();
                var month = date.getMonth() + 1;
                var day = date.getDate();
                var hour = date.getHours();
                var minute = date.getMinutes();
                var second = date.getSeconds();
                // format data
                var monthSTR = month.toString();
                if (month < 10) {monthSTR = "0" + month}
                var daySTR = day.toString();
                if (day < 10) {daySTR = "0" + day}
                var hourSTR = hour.toString();
                if (hour < 10) {hourSTR = "0" + hour}
                var minuteSTR = minute.toString();
                if (minute < 10) {minuteSTR = "0" + minute}
                var secondSTR = second.toString();
                if (second < 10) {secondSTR = "0" + second}
                
                this.date = year + "-" + monthSTR + "-" + daySTR + " " + hourSTR + ":" + minuteSTR + ":" + secondSTR;
                this.temperature = json.main.temp;
                this.tempHigh = json.main.temp_max;
                this.tempLow = json.main.temp_min;
                this.humidity = json.main.humidity;
                this.pressure = json.main.pressure;
                // grab all conditions
                var conditions = "";
                for (const element of json.weather) {
                    conditions = conditions + element.main + ", "
                }
                conditions = conditions.slice(0, -2); // remove exta comma and space
                this.conditions = conditions;

                this.weatherLoaded = 1;
                console.log("No errors calling weather API")
            })
            .catch(err => {
                this.weatherLoaded = -1;
                console.log("Error calling weather API")
            })
        },
        LocationAPICall: function() {
            console.log("Location API Call starting...")
            var locationAPIKey = "0ow9x2FVmLjrfqF7eDQJD0PKsd4tafyhFtLYlWCP";
            fetch("https://api.ipbase.com/v2/info?apikey=" + locationAPIKey)
            .then(response => response.json())
            .then(json => {
                console.log(json);
                this.city = json.data.location.city.name;
                this.region = json.data.location.region.name;
                this.country = json.data.location.country.name;
                this.latitude = json.data.location.latitude;
                this.longitude = json.data.location.longitude;
                
                this.locationLoaded = 1;
                console.log("No errors calling location API")

                // call weather API
                return this.CurrentConditionsAPICall();
            })
            .then(json => {
                return this.ForecastAPICall();
            })
            .catch(err => {
                this.locationLoaded = -1;
                this.weatherLoaded = -1;
                console.log("Error calling location API")
            })
        },
        APICalls() {
            console.log("executing all APICalls")
            this.LocationAPICall();
        },
        rotateState(ev) {
            switch(ev.currentTarget.getAttribute('style')) {
                 // unlikely
                case "background-color: red;":
                    ev.currentTarget.setAttribute('style', "background-color: gray;");
                    this.unlikelyCounter = this.unlikelyCounter - 1;
                    this.neutralCounter  = this.neutralCounter  + 1;
                    break;
                // neutral
                case "background-color: gray;": 
                    ev.currentTarget.setAttribute('style', "background-color: green;");
                    this.neutralCounter  = this.neutralCounter  - 1;
                    this.likelyCounter   = this.likelyCounter   + 1;
                    break;
                // likely
                case "background-color: green;":
                    ev.currentTarget.setAttribute('style', "background-color: red;");
                    this.likelyCounter   = this.likelyCounter   - 1;
                    this.unlikelyCounter = this.unlikelyCounter + 1;
                    break;
            }
        },
    },
    mounted: function() {
        this.APICalls();
    },
}).mount('#app')
