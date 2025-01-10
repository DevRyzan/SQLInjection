MySQL Db Connection

***** Important If you have any issue about protocols, port, IPs, just let me know. *****

***** Important-2 There is no BR in our code or Db, so if you keep testing the same code (main.py), same user data (admin, user1, user2) will be added every time. This is not a problem but good to know. *****

### MacOS ###

-Download docker
-brew install python3

#create an image on your docker 

-docker run --name mysqlserver \
    -e MYSQL_ROOT_PASSWORD=MyStrongPassword \
    -e MYSQL_DATABASE=localmysqldb \
    -p 3306:3306 -d mysql:latest

-pip install mysql-connector-python sqlalchemy

### Windows ###

# Also you dont have to use Docker. 
# if you mind fallow it 

-pip install mysql-connector-python sqlalchemy

-docker run --name mysqlserver -e MYSQL_ROOT_PASSWORD=MyStrongPassword -e MYSQL_DATABASE=localmysqldb -p 3306:3306 -d mysql:latest



# next step
-Change your connectionstring on your local "DbConfig.py" class
-python3 main.py

# The result : 
📦 Tables Are Creating...
✅ Tables Created.
🌱 Seed Data User...
✅ User Created: admin
✅ User Created: user1
✅ User Created: user2
✅ Seed Data added!

# Check your DB

#query
-SELECT * FROM users;

APIs libs 

pip install fastapi uvicorn passlib python-jose
pip install fastapi uvicorn sqlalchemy passlib python-multipart

uvicorn src.Infrastructure.WebAPI.UserAPI:app --reload

pip install fastapi
pip install uvicorn

pip install fastapi uvicorn sqlalchemy pymysql passlib



###For data migration 

These libraries are necessary for migrations and database interaction.
-pip install alembic mysql-connector-python sqlalchemy

Creates the base alembic folder structure.
-alembic init migrations

Locate sqlalchemy.url and set your database connection string:
-sqlalchemy.url = mysql+mysqlconnector://root:password@localhost:3306/localmysqldb


Add your model’s metadata for migrations:

from myapp.models import Base  # Replace `myapp.models` with your module
target_metadata = Base.metadata

Automatically generate migration files based on model changes.
-alembic revision --autogenerate -m "Initial migration"


Applies all migrations to the database.
-alembic upgrade head