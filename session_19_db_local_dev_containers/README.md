## Containerised databases in local development with PostgreSQL, Alembic, and SQLAlchemy

Ensure Postgres not running 

`sudo systemctl status postgresql`

`sudo systemctl stop postgresql`

Start database in container

`docker run --detach --name test-db --rm --env POSTGRES_PASSWORD=mypw --env POSTGRES_USER=myadmin --env POSTGRES_DB=demo5 --publish 5432:5432 postgres:13.4-buster`

Connect to database via psql shell 

- `psql --host localhost --username myadmin --dbname demo5`
- Check connection details `\c`
- Display tables `\dt`
- Exit `\q`

Stop the database container `docker container stop test-db`

Build and run the database migration and seeding container

`docker build --no-cache --tag demo5-db --file db/Dockerfile .`

`docker run --rm --net=host demo5-db`

Use Docker volume to persist the data in the database

`docker run --detach --name test-db --rm --env POSTGRES_PASSWORD=mypw --env POSTGRES_USER=myadmin --env POSTGRES_DB=demo5 --publish 5432:5432 --mount 'type=volume,source=test-db-vol,target=/var/lib/postgresql/data' postgres:13.4-buster`

Check volume has been created `docker volume ls`

Remove volume `docker volume rm test-db`

Build and run the web server container

`docker build --no-cache --tag demo5-web --file web/Dockerfile .`

`docker run --rm --net=host --publish 8000:8000 demo5-web`
