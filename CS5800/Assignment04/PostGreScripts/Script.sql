/* Creating the Database */
CREATE DATABASE assignment;

/* Selecting the Database */
\c assignment;

/* Create Table 'users' */
CREATE TABLE users (
id INTEGER NOT NULL,
name VARCHAR(40) NOT NULL,
CONSTRAINT users_pk PRIMARY KEY (id)
);

/* Create Table 'comments' */
CREATE TABLE comments (
id INTEGER NOT NULL,
id_user INTEGER NOT NULL,
text VARCHAR(400) NOT NULL,
CONSTRAINT comments_pk PRIMARY KEY (id, id_user)
);

/* Alter Table 'comments' */
ALTER TABLE comments ADD CONSTRAINT users_comments_fk
FOREIGN KEY (id_user)
REFERENCES users (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

