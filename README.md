# URL Shortener
This is a lap 4 coding challenge which involved building a URL shortener in Python, using Flask. An external Heroku PostgreSQL database is used to store the URLs, both original and the shortened version, as well as the date created and number of times visited. Bulma framework was used for parts of the styling.

## Installation and Usage
### Installation
1. Clone the repo
2. Run `pipenv shell` to enter the virtual environment
3. Run `pipenv install` to install the dependencies

### Usage
1. Run `flask run` to start the server
2. Navigate to `http://localhost:5000/` to see the homepage
3. You don't have the .env details yet, so you'll need to enter the details manually
It's not especially secret so make a .env file in root with these details:
```
SECRET_KEY=verysecretkey
DATABASE_URL=sqlite:///shorty.db
APP_SETTINGS=config.DevelopmentConfig
FLASK_APP=core
```
4. Or just use the deployed version at https://gebrurl.herokuapp.com/

## Wins and Challenges
### Wins
- URL shortener works
- Database is working
- Heroku deployment works

### Challenges
- Deploying with the SQLite database during deployment was a challenge

