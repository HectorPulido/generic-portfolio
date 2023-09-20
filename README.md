# Generic portfolio

## Setup Django

1. Configure your heroku project, save the name, you will need the Heroku Postgresql addon

2. Build the docker development and run it to make sure everything is ok

```
docker build -t web:latest .
docker run -d --name <herokuname> -e "PORT=8765" -e "DEBUG=0" -p 8007:8765 web:latest
```

3. You can deactivate like this
```
docker stop <herokuname>
docker rm <herokuname>
```

4. You can upload your project with this commands
```
docker run -d --name <herokuname> -e "PORT=8765" -e "DEBUG=0" -p 8007:8765 web:latest
heroku container:login
heroku container:push web -a <herokuname>
heroku container:release web -a <herokuname>
```

5. Create your user with
```
heroku run python manage.py createsuperuser -a <herokuname>
```

6. Enter to your proyect from this url
```
http://<herokuname>.herokuapp.com/admin
```
