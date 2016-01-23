CREATE SCHEMA usersdb;

CREATE TABLE User(
email PRIMARY KEY,
password varchar(20),
user_type enum('0','1','2') NOT NULL,
first_name varchar NOT NULL,
last_name varchar NOT NULL);

CREATE TABLE GoesToUni(
email NOT NULL REFERENCES Mentor,
school varchar NOT NULL REFERENCES Universities,
major varchar NOT NULL REFERENCES,
Year integer,
PRIMARY KEY(email, school));

CREATE TABLE GoesToHS(
email NOT NULL REFERENCES Mentor,
school varchar NOT NULL,
grade integer,
PRIMARY KEY(email, school));

CREATE TABLE Universities(
uni PRIMARY KEY);