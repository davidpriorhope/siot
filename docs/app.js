var button = document.querySelector('.button')
var inputValue = document.querySelector('.inputValue')
var calc_text = document.querySelector('.calc_text');

const coef_weather = -0.0005515359850265903;

const coef_layer = 0.06789060123891683;

const int = 1.058203868005206;

const score = 0.29;


button.addEventListener('click',function(){
    fetch('https://api.openweathermap.org/data/2.5/weather?q='+inputValue.value+'&appid=ada8d9cc126cf4404e8e2bae94450f3e&units=metric')
    .then(response => response.json())
    .then(data => {
        var tempValue = parseFloat(data['main']['temp']);

        var optimal_layers = Math.round((1-coef_weather*tempValue-int)/coef_layer);

        calc_text.innerHTML = 'For ' + inputValue.value + ' the temperature is ' + tempValue + '&deg;C it is recommended to wear: ' + optimal_layers +' layers. The R-squared from machine learning is '+ score;

    })

.catch(err => alert("Wrong city name!"))
})


console.log()