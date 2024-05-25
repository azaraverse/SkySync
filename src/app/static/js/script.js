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
    const iconCode = data.weather.weather[0].icon;
    const icon = `https://openweathermap.org/img/wn/${iconCode}@4x.png`;
    const date = new Date(data.weather.dt * 1000); // convert seconds to milliseconds since the epoch
    const dateString = date.toLocaleDateString('en-Us', { weekday: 'short', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' });
    const weatherInfo = `
        <div class="text-center forecast-item-current">
            <img id="weather-icon" alt="${data.weather.weather[0].description}" src="${icon}">
            <p><strong>${data.weather.name}, ${data.weather.sys.country}</strong></p>
            <p>${dateString}</p>
            <h1 class="be-vietnam-pro-thin">${Math.floor(data.weather.main.temp)}°</h1>
            <p>${capitaliseWords(data.weather.weather[0].description)}<p>
            <p>H:${Math.floor(data.weather.main.temp_max)}° L:${Math.floor(data.weather.main.temp_min)}°</p>
            <p></p>
            <p class="mt-3">Feels like: ${Math.floor(data.weather.main.feels_like)}°</p>
            <div class="mt-3 pad-bottom">
                <p>Humidity: ${Math.floor(data.weather.main.humidity)}%</p>
                <p>Wind Speed: ${Math.floor(data.weather.wind.speed)} m/s</p>
            </div>
        </div>`;
    $('#weather-info').html(weatherInfo);
  }

  // Function to display forecast data
  function displayForecastData (data) {
    let hourlyForecastInfo = '<p class="text-center">3-Hour Interval Forecast</p>';
    let forecastInfo = '<p class="text-center">5-Day Forecast</p>';
    const today = new Date();
    today.setDate(today.getDate()); // get today's date

    // Filter forecast data for the next five days and hourly data for tomorrow
    const dailyForecastData = data.list.filter(item => {
      const date = new Date(item.dt_txt);
      return date.getHours() === 12 && date.getDate() !== today.getDate(); // filter 12 noon data for the next five days except today
    });

    // Get the first 8 items for today's hourly forecast
    const hourlyForecastData = data.list.slice(0, 8);

    // Display hourly forecast for today
    hourlyForecastInfo += '<div class="scrollable-horizontal">';
    hourlyForecastData.forEach(item => {
      const date = new Date(item.dt_txt);
      const iconCode = item.weather[0].icon;
      const icon = `https://openweathermap.org/img/wn/${iconCode}.png`
      const dateString = date.toLocaleDateString('en-US', { weekday: 'short', hour: '2-digit', minute: '2-digit' });
      hourlyForecastInfo += `
            <div class="forecast-item">
                <p class="text-center">${dateString}</p>
                <img src="${icon}" alt="${item.weather[0].description}">
                <p class="text-center">${Math.floor(item.main.temp)}°</p>
                <p class="text-center">${capitaliseWords(item.weather[0].description)}</p>
            </div>`;
    });
    hourlyForecastInfo += '</div>';

    // Display daily forecast for the next five days
    forecastInfo += '<div class="scrollable-horizontal">'
    dailyForecastData.forEach(item => {
      const date = new Date(item.dt_txt);
      const iconCode = item.weather[0].icon;
      const icon = `https://openweathermap.org/img/wn/${iconCode}.png`
      const dateString = date.toLocaleDateString('en-US', { weekday: 'short', month: 'short', day: 'numeric', year: 'numeric' });
      forecastInfo += `
        <div class="forecast-item">
            <p class="text-center">${dateString}</p>
            <img src="${icon}" alt="${item.weather[0].description}">
            <p class="text-center">${Math.floor(item.main.temp)}°</p>
            <p class="text-center">${capitaliseWords(item.weather[0].description)}</p>
        </div>`;
    });
    $('#forecast-info').html(hourlyForecastInfo + forecastInfo);
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
    console.log(city);
    if (city) {
      $.ajax({
        url: '/search',
        type: 'POST',
        data: { city },
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
