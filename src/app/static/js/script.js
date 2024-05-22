/* eslint-disable no-alert */
document.addEventListener('DOMContentLoaded', function () {
  console.log('JavaScript is loaded and working!');
  // Loading spinner
  function showLoadingSpinner () {
    $('#loading-spinner').show();
  }

  function hideLoadingSpinner () {
    $('#loading-spinner').hide();
  }

  // Function to get weather data using coordinates
  function getWeatherByCoords (lat, lon) {
    showLoadingSpinner();
    $.ajax({
      url: '/get_weather_by_coords',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({
        latitude: lat,
        longitude: lon
      }),
      success: function (data) {
        hideLoadingSpinner();
        if (data.error) {
          alert('Error fetching weather data: ' + data.error);
        } else {
          displayWeatherData(data);
          getForecastByCoords(lat, lon);
        }
      },
      error: function (error) {
        hideLoadingSpinner();
        console.error('Error:', error);
        alert('Error fetching weather data. Please try again.');
      }
    });
  }

  // Function to get forecast data using coordinates
  function getForecastByCoords (lat, lon) {
    showLoadingSpinner();
    $.ajax({
      url: '/forecast',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({
        lat,
        lon
      }),
      success: function (data) {
        hideLoadingSpinner();
        if (data.error) {
          alert('Error fetching forecast data: ' + data.error);
        } else {
          displayForecastData(data);
        }
      },
      error: function (error) {
        hideLoadingSpinner();
        console.error('Error:', error);
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
    console.log(data);
    let date = new Date(data.weather.dt * 1000) // convert seconds to milliseconds since the epoch
    let dateString = date.toLocaleDateString('en-Us', { weekday: 'short', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' })
    const weatherInfo = `
        <div class="text-center forecast-item-current">
            <p><strong>${data.weather.name}, ${data.weather.sys.country}</strong></p>
            <p>${dateString}</p>
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
  function displayForecastData (data) {
    let forecastInfo = '<p class="text-center">5-Day Forecast</p>';
    forecastInfo += '<div class="scrollable-horizontal"></div>';
    data.list.forEach(item => {
        let date = new Date(item.dt_txt)
        let dateString = date.toLocaleDateString('en-US', { weekday: 'long', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' })
      forecastInfo += `
        <div class="forecast-item">
            <p class="text-center">${dateString}</p>
            <p class="text-center">${Math.floor(item.main.temp)}° - ${capitaliseWords(item.weather[0].description)}</p>
        </div>`;
    });
    forecastInfo += '</div>'
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
    hideLoadingSpinner();
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

  // Handle form on submission
  $('form').on('submit', function (event) {
    event.preventDefault();
    showLoadingSpinner();
    const city = $('input[name="city"]').val();
    console.log(city)
    if (city) {
      $.ajax({
        url: '/search',
        type: 'POST',
        data: { city: city },
        success: function (data) {
          hideLoadingSpinner();
          if (data.error) {
            alert('Error fetching weather data: ' + data.error);
          } else {
            displayWeatherData(data);
            const lat = data.weather.coord.lat;
            const lon = data.weather.coord.lon;
            getForecastByCoords(lat, lon);
          }
        },
        error: function (error) {
          hideLoadingSpinner();
          console.error('Error:', error);
          alert('Error fetching weather data. Please try again.');
        }
      });
    }
  });
});
