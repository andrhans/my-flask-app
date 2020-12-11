# Research and sources...

* Database Design
https://flaskage.readthedocs.io/en/latest/database_design.html

* Databases and SQL
https://www.tutorialspoint.com/python_network_programming/python_databases_and_sql.htm

* Discover Flask:
https://realpython.com/introduction-to-flask-part-2-creating-a-login-page/
https://www.youtube.com/watch?v=_vrAjAHhUsA

* Flask CRUD (Create, Retrieve, Update, Delete)
https://www.askpython.com/python-modules/flask/flask-crud-application

* Flask-SQLAlchemy:
https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/
https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_using_query.htm
https://docs.sqlalchemy.org/en/13/orm/tutorial.html#querying-with-joins
https://www.javatpoint.com/flask-sqlalchemy

* Flask-Login:
https://flask-login.readthedocs.io/en/latest/#login-example

* Flask HTTP methods:
https://pythonbasics.org/flask-http-methods/

* Flask Login Required Decorator:
https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/#login-required-decorator

* Postman investigation
https://learning.postman.com/docs/writing-scripts/script-references/test-examples/

* Json
https://pythonbasics.org/json/
https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask

* Login with flask, python and mysql:
https://codeshack.io/login-system-python-flask-mysql/

* Message flashing:
https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/

* MotorAPI:
https://www.motorapi.dk/

* Pythonanywhere: connecting to MySQL
https://danielcorcoranssql.wordpress.com/2019/04/24/pythonanywhere-connecting-to-mysql-creating-virtual-environment/

* SQL:
https://www.w3schools.com/sql/sql_examples.asp

* Simple Apps:
https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972

## Interacting with the database has challenging

As I was unable to use cursors, I reached out to create the tables myself with the following strings,
from the MySQL console:

To create the users table:
CREATE TABLE users (id int(11) not null auto_increment primary key, username varchar(128) not null, password varchar(128) not null, cvr varchar (80) not null, email varchar(129));

I realized I couldn't insert dummy data and realized I had to alter the email column so it would be *not null*, so:
alter table users modify email varchar(128) not null;

Afterwards, inserted the following on the command line:
INSERT INTO users (username,password,cvr,email) VALUES('admin',PASSWORD('admin'),'12345','a@example.com'));

Then, I tried to register new users, which was a successful operation.

What is missing right now is the login with the connection to the database.

To create the cars table:
CREATE TABLE cars (id int(11) not null auto_increment primary key, registration_id varchar(128) not null, brand varchar(80) not null, model varchar(80) not null, version varchar(128) not null, fuel_type varchar(80) not null, model_year int(4) not null, engine_power int(3) not null, fuel_efficiency varchar(80) not null, engine_cylinders int(11) not null, top_speed decimal(10,2) not null, doors int(1) not null, minimum_seats int(1) not null, axles int(1) not null, drive_axles int(1) not null);

Insert dummy car:
INSERT INTO cars (registration_id,brand,model,version,fuel_type,model_year,engine_power,fuel_efficiency,engine_cylinders,top_speed,doors,minimum_seats,axles,drive_axles) VALUES('AB12345','RENAULT','Captur','dCi 90','Diesel','2013','66','27.8','4','171','4','5','2','1');
INSERT INTO cars (registration_id,brand,model,version,fuel_type,model_year,engine_power,fuel_efficiency,engine_cylinders,top_speed,doors,minimum_seats,axles,drive_axles) VALUES('BX84828','MAZDA','MX-5','2.0 SKYACTIV-G 160 HK Roadster Man.','Gasoline','2015','118','14.5','4','214','2','2','2','1');

