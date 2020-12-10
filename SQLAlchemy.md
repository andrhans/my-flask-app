## Interacting with the database has been quite challenging.

As I was unable to use cursors, I reached out to create the tables myself with the following strings,
from the MySQL console:

To create the users table:
CREATE TABLE users (id int(11) not null auto_increment primary key, username varchar(128) not null, password varchar(128) not null, cvr varchar (80) not null, email varchar(129));

I realized I couldn't insert dummy data and realized I had to alter the email column so it would be *not null*.

CREATE TABLE cars (id int(11) not null auto_increment primary key, registration_id varchar(128) not null, brand varchar(80) not null, model varchar(80) not null, version varchar(128) not null, fuel_type varchar(80) not null, model_year int(4) not null, engine_power int(3) not null, fuel_efficiency varchar(80) not null, engine_cylinders int(11) not null, top_speed decimal(10,2) not null, doors int(1) not null, minimum_seats int(1) not null, axles int(1) not null, drive_axles int(1) not null);

