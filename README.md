# GIS Demo

## WWI THOR and World Borders 1880, 1914, 1920

## Endpoints
Live url: https://wwi-thor-api.herokuapp.com

```
/api/v1/borders/
/api/v1/missions/
/api/v1/aircraft/
/api/v1/weapons/
```
## Getting Started

### Deployment to your own heroku stack

1. create an account on [heroku.com](https://heroku.com)

2. install [heroku cli](https://devcenter.heroku.com/articles/heroku-cli)

```
brew tap heroku/brew && brew install heroku
```

3. create a heroku app

```
heroku apps:create my-unique-name
```

4. Add and [configure postgis db](https://devcenter.heroku.com/articles/heroku-postgres-extensions-postgis-full-text-search)

```
$ heroku addons:create heroku-postgresql:hobby-dev
$ echo 'show extwlist.extensions' | heroku pg:psql
$ heroku pg:psql
=> CREATE extension postgis;
```

5. Get the DATABASE_URL and split it into individual env vars, add the result to  your `.env`

```
$ heroku config
```

6. Push the environment variables to heroku

```
cat geodjango/.env | xargs heroku config:set 
```

7. [Deploy](https://devcenter.heroku.com/articles/deploying-django)

```
git push heroku main
```

8. Migrate and load data

```
heroku run python manage.py migrate
heroku run python manage.py shell < seed.py
```
