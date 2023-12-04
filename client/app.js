function onClickedEstimateCalories() {
  console.log("Estimate calories button clicked");
  var gender = document.getElementById("uiGenders");
  var age = document.getElementById("uiAge");
  var height = document.getElementById("uiHeight");
  var weight = document.getElementById("uiWeight");
  var duration = document.getElementById("uiDuration");
  var heart_rate = document.getElementById("uiHeart_rate");
  var body_temp = document.getElementById("uiBody_temp");
  var estCalories = document.getElementById("uiEstimatedCalories");

  // var url = "http://127.0.0.1:5000/predict_home_price"; //Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  var url = "http://127.0.0.1:5000/predict_cal";
  $.post(url, {
      age: parseFloat(age.value),
      height: parseFloat(height.value),
      weight: parseFloat(weight.value),
      duration: parseFloat(duration.value),
      heart_rate: parseFloat(heart_rate.value),
      body_temp: parseFloat(body_temp.value),
      gender: gender.value
  },function(data, status) {
      console.log(data.estimated_calories);
      estCalories.innerHTML = "<h2>" + data.estimated_calories.toString() + " calories</h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );
  // var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx
  //var url = "/api/get_location_names";// Use this if  you are using nginx, i think  deployment
  var url = "http://127.0.0.1:5000/get_gender_names";
  $.get(url,function(data, status) {
      console.log("got response for get_location_names request");
      if(data) {
          var genders = data.genders;
          var uiGenders = document.getElementById("uiGenders");
          $('#uiGenders').empty();
          for(var i in genders) {
              var opt = new Option(genders[i]);
              $('#uiGenders').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;
