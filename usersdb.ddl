CREATE SCHEMA usersdb;

CREATE TABLE User(
email PRIMARY KEY,
password varchar,
user_type integer NOT NULL,
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
Year integer,
PRIMARY KEY(email, school));

CREATE TABLE Universities(
uni PRIMARY KEY);