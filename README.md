# pAIrFlaskProject

This project is an example of a Flask Microservices app. It has a handler app which receives commands, as well as individual flask apps for tracking Temperature and Humidity Data, Feeding logs, and Nutramigen formulat calculations. It was built by me with assistance from ChatGPT which provided boilerplate code for the flask apps and helpful tips on developing in Flask. It also has a Frontend React app inside a Docker container that can communicate with the individual services. It also has individual Postgres volumes for formula calculations and temperature data so that those databases can be updated and modified independently without affecting data from the other apps.

## Usage

* Copy env.example and provide the required values
* Docker compose up to start all services
