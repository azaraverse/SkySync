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
          displayWeatherData(data)
          getForecastByCoords(lat, lon);
        }
      },
      error: function (error) {
        console.error('Error:', error);
        alert('Error fetching weather data. Please try again.')
      }
    });
  }

  // Function to get forecast data using coordinates
  function getForecastByCoords (lat, lon) {
    $.ajax({
        url: '/forecast',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            lat: lat,
            lon: lon
        }),
        success: function (data) {
            if (data.error) {
                alert('Error fetching forecast data: ' + data.error);
            } else {
                displayForecastData(data);
            }
        },
        error: function (error) {
            console.error('Error:', error)
            alert('Error fetching forecast data. Please try again.');
        }
    });
  }

  // function to capitalise the first letter of a word
  function capitaliseWords (str) {
    return str.replace(/\b\w/g, function (char) {
        return char.toUpperCase();
    });
  }

  // Function to display weather data
  function displayWeatherData (data) {
    const weatherInfo = `
        <div class="text-center forecast-item">
            <p><strong>${data.weather.name}, ${data.weather.sys.country}</strong></p>
            <h1>${Math.floor(data.weather.main.temp)}°</h1>
            <p>${capitaliseWords(data.weather.weather[0].description)}<p>
            <div class="row justify-content-center">
                <div class="col-auto">
                    <p>High: ${Math.floor(data.weather.main.temp_max)}°</p>
                </div>
                <div class="col-auto">
                    <p>Low: ${Math.floor(data.weather.main.temp_min)}°</p>
                </div>
            </div>
            <p class="mt-3">Feels like: ${Math.floor(data.weather.main.feels_like)}°</p>
            <div class="mt-3">
                <p>Humidity: ${Math.floor(data.weather.main.humidity)}%</p>
                <p>Wind Speed: ${Math.floor(data.weather.wind.speed)} km/s</p>
            </div>
        </div>`;
    $('#weather-info').html(weatherInfo);
  }

  // Function to display forecast data
  function displayForecastData(data) {
    let forecastInfo = '<h2 class="text-center">5-Day Forecast</h2>';
    data.list.forEach(item => {
      forecastInfo += `
        <div class="forecast-item">
          <h4 class="text-center">${new Date(item.dt_txt).toLocaleDateString()}</h4>
          <p class="text-center">${Math.floor(item.main.temp)}° - ${capitaliseWords(item.weather[0].description)}</p>
        </div>`;
    });
    $('#forecast-info').html(forecastInfo);
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
