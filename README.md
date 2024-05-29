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
