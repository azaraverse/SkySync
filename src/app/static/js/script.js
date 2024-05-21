/* eslint-disable no-alert */
document.addEventListener('DOMContentLoaded', function () {
  // Function to get weather data using coordinates
  function getWeatherByCoords(lat, lon) {
    $.ajax({
      url: '/get_weather_by_coords',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({
        lat: lat,
        lon: lon
      }),
      success: function (data) {
        if (data.error) {
          alert('Error fetching weather data: ' + data.error);
        } else {
          displayWeatherData(data);
        }
      },
      error: function (error) {
        console.error('Error:', error);
        alert('Error fetching weather data. Please try again.')
      }
    });
  }

  // Function to display weather data
  function displayWeatherData (data) {
    const weatherInfo = `
        <div class="text-center">
            <h6><strong>${data.name}, ${data.sys.country}</strong></h6>
            <h1>${Math.floor(data.main.temp)}°</h1>
            <h6>${data.weather[0].description}</h6>
            <div class="row justify-content-center">
                <div class="col-auto">
                    <h6>High: ${Math.floor(data.main.temp_max)}°</h6>
                </div>
                <div class="col-auto">
                    <h6>Low: ${Math.floor(data.main.temp_min)}°</h6>
                </div>
            </div>
            <h6 class="mt-3">Actually feels like: ${Math.floor(data.main.feels_like)}°</h6>
            <div class="mt-3">
                <h6>Humidity: ${Math.floor(data.main.humidity)}%</h6>
                <h6>Wind Speed: ${Math.floor(data.wind.speed)} km/s</h6>
            </div>
        </div>`;
    $('#weather-info').html(weatherInfo);
  }

  // Function to handle geolocation success
  function showPosition (position) {
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;
    getWeatherByCoords(lat, lon);
  }

  // Function to handle geolocation error
  function showError (error) {
    switch (error.code) {
      case error.PERMISSION_DENIED:
        alert('User denied the request for Geolocation.');
        break;
      case error.POSITION_UNAVAILABLE:
        alert('Cannot determine location.');
        break;
      case error.TIMEOUT:
        alert('The request to get user location timed out.');
        break;
      case error.UNKNOWN_ERROR:
        alert('An unknown error occured.');
        break;
    }
  }

  // Check if geolocation is supported by the browser
  if (navigator.geolocation) {
    // Request geolocation
    navigator.geolocation.getCurrentPosition(showPosition, showError);
  } else {
    alert('Geolocation is not supported by this browser.');
  }
});
