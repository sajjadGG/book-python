CREATE TABLE people (
    id integer primary key auto increment,
    first_name varchar(20),
    last_name varchar(20)
);

INSERT INTO people VALUES ("José", "Jiménez");
INSERT INTO people (first_name, last_name) VALUES ("Max", "Peck");

SELECT * FROM people;

1|José|Jiménez
2|Max|Peck