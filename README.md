# SkySync
[SkySync](https://www.muqitazara.tech/) is a web application built using [python](https://www.python.org), with [flask](https://flask.palletsprojects.com/en/3.0.x/) as framework, [Gunicorn](https://gunicorn.org/), [Nginx](https://nginx.org/en/), HTML, CSS (local css and [bootstrap](https://getbootstrap.com/)) and [JavaScript](https://www.javascript.com/). It falls on the [OpenWeatherMap](https://openweathermap.org) API to retrieve, extract and display weather data using web scraping techniques. This ensures a scalable and efficient weather service.

## Table of Contents
- [SkySync](#skysync)
    - [Table of Contents](#table-of-contents)
    - [Features](#features)
    - [Demo](#demo)
    - [Installation](#installation)
        - [Prerequisites](#prerequisites)
        - [Clone the Repository](#clone-the-repository)
        - [Install Dependencies](#install-dependencies)
    - [Configuration](#configuration)
    - [Running the Application](#running-the-application)
        - [Using Flask's Development Server](#using-flasks-development-server)
        - [Using Gunicorn](#using-gunicorn)
        - [Setting up Nginx](#setting-up-nginx)
    - [Usage](#usage)
    - [Contributions](#contributions)
    - [Bugs](#bugs)

## Features
- Utilises geolocation (device's location) to retrieve weather data
- Real-time weather updates
- Weather forecasts (3-hour & 5-days forecast)
- Responsive design
- Easy integration with external APIs
- Scalable using Gunicorn and Nginx

## Demo
Check out the live demo via: [SkySync Demo](https://www.muqitazara.tech)

## Installation
### Prerequisites
- Python 3.8.10 or higher
- Flask
- Gunicorn
- Nginx
- Git

### Clone the Repository
```bash
git clone https://github.com/gitloper-azara/SkySync.git
cd SkySync
```

### Install Dependencies
```bash
cd src
pip install -r requirements.txt
```

## Configuration
Configure these environment variables in a .env file (These need to be configured in a `gunicorn` service file for deployment to production).
See [gunicorn.service](./src/server_side_config/gunicorn.service)
`FLASK_APP=run.py`
`FLASK_ENV=development`
`WEATHER_API_KEY=weather_api_key`
`WEATHER_API_HOST=0.0.0.0`
`WEATHER_API_PORT=5003`
`PYTHONPATH=path/to/SkySync/src`

Make sure to replace `weather_api_key` with an actual weather API key from [OpenWeatherMap](https://openweathermap.org).

## Running the Application
### Using Flask's Development Server
```bash
export FLASK_APP=run.py
export FLASK_ENV=development
export PYTHONPATH=path/to/SkySync/src
flask run
```

### Using Gunicorn
Refer to [gunicorn.service](./src/server_side_config/gunicorn.service) and insert content after the `nano` command below.
```bash
nano /etc/systemd/system/gunicorn.service
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

### Setting up Nginx
Refer to [nginx.default](./src/server_side_config/nginx.default) and insert content after the `nano` command below.
```bash
nano /etc/nginx/sites-available/default
sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```
Only restart nginx when `nginx -t`(checking nginx syntax) passes without errors!

## Usage
Visit the website at [SkySync](https://www.muqitazara.tech) to get real-time weather updates.

## Contributions
Contributions are highly welcome. Kindly fork this repository, make necessary contributions and submit a pull request.

## Bugs
No known bugs at this point.
