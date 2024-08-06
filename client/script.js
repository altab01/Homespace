var get_url = 'http://127.0.0.1:5000/get_location_names';
var predict_url = 'http://127.0.0.1:5000/predict_price';

const cityName= document.getElementById('city');

const getCity=()=>{
    const cityName = document.getElementById('city');
    const cityVal=(cityName.value);
    return cityVal;
}

const get_bkh=()=>{
     const bhk=document.getElementsByName('bhk');
     for(let i in bhk){
        if(bhk[i].checked){
            return parseInt(i)+1;
        }
     }
     return -1;
}

const get_bath=()=>{
    const bath=document.getElementsByName('bath');
    for(let i in bath){
       if(bath[i].checked){
           return parseInt(i)+1;
       }
    }
    return -1;
}



function onCityChange() {
    const city=getCity();
    console.log(city)
    $.get(get_url,{city:city}, function(data, status) {
        if (data) {
            var location = data.locations;
            const dropdown = document.getElementById('dropdown');
            dropdown.innerHTML = '';
            dropdown.appendChild(new Option("OTHER"));
            location.forEach(item => {
                const option = new Option(item.toUpperCase());
                dropdown.appendChild(option);
            });
            
        }
    });
}

document.getElementById('city').addEventListener('change', onCityChange);

const btn = document.getElementById('btn');
btn.addEventListener('click', (event)=>{
    let bhk = get_bkh();
    let bath = get_bath();

    const sqftInput = document.getElementById('sqft');
    const sqftValue = sqftInput.value;
  

    const loc = document.getElementById('dropdown');
    const locationValue = (loc.value).toLowerCase();
    const cityVal=getCity();
    console.log(cityVal);
    
    $.post(predict_url,{
          city:cityVal,
          sqft:parseFloat(sqftValue),
          location:locationValue,
          bath:bath,
          bhk:bhk
    },function(data,status){
        const predicted_price = document.getElementById('predicted_price');
        predicted_price.innerHTML="<h4>"+data.estimated_price.toString()+"Lakh</h4>";

    })

    event.preventDefault();
});

