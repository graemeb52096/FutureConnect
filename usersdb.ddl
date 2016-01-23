CREATE SCHEMA usersdb;

USE usersdb;

CREATE TABLE Users (
    email VARCHAR(255) NOT NULL,
    password VARCHAR(20),
    user_type ENUM('0','1','2') NOT NULL,
    bio VARCHAR(1500),
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,

    PRIMARY KEY (email)
);

CREATE TABLE Majors (
    major VARCHAR(255) NOT NULL,

    PRIMARY KEY (major)
);

CREATE TABLE Universities (
    uni VARCHAR(255) NOT NULL,

    PRIMARY KEY (uni)
);

CREATE TABLE GoesToUni (
    email VARCHAR(255) NOT NULL,
    school VARCHAR(255) NOT NULL,
    major VARCHAR(255) NOT NULL,
    Year INTEGER,

    PRIMARY KEY (email, school, major),

    FOREIGN KEY (email) REFERENCES Users (email),
    FOREIGN KEY (school) REFERENCES Universities (uni),
    FOREIGN KEY (major) REFERENCES Majors (major)
);

CREATE TABLE GoesToHS (
    email VARCHAR(255) NOT NULL,
    school VARCHAR(255) NOT NULL,
    grade INTEGER,

    PRIMARY KEY (email, school),

    FOREIGN KEY (email) REFERENCES Users (email)
);