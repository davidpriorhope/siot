var button = document.querySelector('.button')
var inputValue = document.querySelector('.inputValue')
var calc_text = document.querySelector('.calc_text');

const desired_temp = 1;

const coef_weather = 0.002011415933145354;

const coef_layer = -0.0036703344530358405;

const lin_int = 1.1395050507863926;

const lin_score = 0.02;

const Ci = 0.0;

const Cw = -0.0820182885958174;

const Cl = -0.8151327550968669;

const CW = -0.0005615545996462551;

const C2 = 0.047547767733024125;

const CL = 0.09667449798666977;

const quad_int = 2.3496928822370524;

const quad_score = 0.9998808457894686;

button.addEventListener('click',function(){
    fetch('https://api.openweathermap.org/data/2.5/weather?q='+inputValue.value+'&appid=ada8d9cc126cf4404e8e2bae94450f3e&units=metric')
    .then(response => response.json())
    .then(data => {
        var tempValue = parseFloat(data['main']['temp']);

        var a = CL;

        var b = C2*tempValue + Cl;
        
        var c = Ci + Cw*tempValue + CW*tempValue**2+quad_int-desired_temp;

        if (((b**2)-4*a*c)>0) {
            var optimal_layers = Math.round((-b+((b**2)-4*a*c)**0.5)/(2*a));

            var score = quad_score

        } else{
            var optimal_layers = Math.round((desired_temp-coef_weather*tempValue-lin_int)/coef_layer);
            var score = lin_score
        }

        calc_text.innerHTML = 'For ' + inputValue.value + ' the temperature is ' + tempValue + '&deg;C it is recommended to wear: ' + optimal_layers +' layers. The R-squared from machine learning is '+ score;

    })

.catch(err => alert("Wrong city name!"))
})


console.log()