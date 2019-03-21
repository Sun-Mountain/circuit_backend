# Circuit App

## Description
Circuit App is a React/Django application that allows users to create circuits and add workouts with specified length of time (in minutes and seconds).

## Frontend
Deployed: http://circuitapp.surge.sh/

Github: https://github.com/Sun-Mountain/circuit_frontend

## Deployed Backend
https://circuit-backend.herokuapp.com/api/

## Tech
This is a React.js frontend and Django backend, styled with CSS.

## Dependencies
**Frontend**
- antd (Ant Design)
- axios
- react
- react-dom
- react-router-dom

**Backend**
- django-cors-headers
- django-rest-auth
- djangorestframework
- gunicorn
- psycopg2-binary
- python3
- whitenoise

## Future
- Add user authorization so that they will only show circuits that the user created.
- Create a timer to run through circuit workouts, countingdown and then prompting the user to start the next workout.
- Make it so that users could choose to have their circuits private or public.
- Users can "favorite" or save circuits from other users to their boards.
- Create a leaderboard for most popular circuits.