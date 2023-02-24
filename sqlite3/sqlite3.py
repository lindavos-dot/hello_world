import sqlite3


# Exercise: interacting with the database

# Display the entries in the movies table using a SELECT statement.
# SELECT * FROM movies;
# SELECT title FROM movies;


# Use the WHERE statement, in combination with SELECT, to display all movies with a rating of exactly 5.
# SELECT * FROM movies WHERE rating = 5;


# Add 5 more movies in your database using INSERT.
# INSERT INTO movies( title, year, rating ) VALUES ( "Memento", 2000, 4 );
# INSERT INTO movies( title, year, rating ) VALUES ( "His Dark Materials", 2018, 5 );
# INSERT INTO movies( title, year, rating ) VALUES ( "Fleabag", 2016, 2 );
# INSERT INTO movies( title, year, rating ) VALUES ( "Mr. Robot", 2015, 5 );
# INSERT INTO movies( title, year, rating ) VALUES ( "The Wire", 2002, 3 );


# Use the SELECT statement again to see if the new movies have indeed been added.
# SELECT title FROM movies;


# Start by creating the new genres table using a CREATE TABLE statement. Define a column for the ID (this will serve as our primary key), and one for the name of the genre.
# CREATE TABLE genre (id_genre INTEGER, name_genre TEXT);


# Add some (5+) genres to the new table using the INSERT statement. Make sure every record has an ID and a name.
# INSERT INTO genre(id_genre, name_genre ) VALUES ("1", "romance");
# INSERT INTO genre(id_genre, name_genre ) VALUES ("2", "action");
# INSERT INTO genre(id_genre, name_genre ) VALUES ("3", "drama");
# INSERT INTO genre(id_genre, name_genre ) VALUES ("4", "fantasy");
# INSERT INTO genre(id_genre, name_genre ) VALUES ("5", "thriller");     


# Display the records in the genres table using SELECT and check if everything is in order.
# SELECT * FROM genre;


# Now, ALTER the movies table by adding a field for referencing to a genre ID. Since the new column will contain an ID, the datatype will be a number. Name it anyway you like (something like genre_id would do perfectly).
# ALTER TABLE movies ADD genre_id INTEGER;


# Next, UPDATE your movies table by supplying every record with a value in the genre_id column, pointing to a record in the genres table.
# UPDATE movies SET genre_id = 1 WHERE title = "The Prince and Me";
# UPDATE movies SET genre_id = 1 WHERE title = "The Prince and Me 2";
# UPDATE movies SET genre_id = 1 WHERE title = "The Prince and Me 3";
# UPDATE movies SET genre_id = 1 WHERE title = "The Prince and Me 4: The Elephant Adventure";
# UPDATE movies SET genre_id = 5 WHERE title = "Memento";
# UPDATE movies SET genre_id = 4 WHERE title = "His Dark Materials";
# UPDATE movies SET genre_id = 3 WHERE title = "Fleabag";
# UPDATE movies SET genre_id = 4 WHERE title = "Mr. Robot";
# UPDATE movies SET genre_id = 2 WHERE title = "The Wire";


# Finally, use a LEFT JOIN on the movies and genres table, matching the IDs. This should combine the tables, showing all movies records along with their genre information.
# SELECT * FROM movies LEFT JOIN genre ON movies.genre_id = genre.id_genre;


# (bonus) Which other join can we use in order to only show records that have genre information (omitting any records without a genre_id)?
# Inner Join


# Geen nieuwe database aanmaken, maar nieuwe Table aanmaken in de bestaande database. Liep vast bij .open FILENAME in CMD. Op deze manier werkt het wel