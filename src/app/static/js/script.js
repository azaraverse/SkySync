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
        <h2>Weather in ${data.name}</h2>
        <ul>
            <li>Temperature: ${data.main.temp}°C</li>
            <li>Feels like: ${data.main.feels_like}°C</li>
            <li>Humidity: ${data.main.humidity}%</li>
            <li>Wind Speed: ${data.wind.speed}m/s</li>
            <li>Conditions: ${data.weather[0].description}</li>
        </ul>`;
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
