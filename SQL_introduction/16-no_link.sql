-- lists all records of the table second table
INSERT INTO second_table VALUES(5, "Aria", 12);
INSERT INTO second_table VALUES(6, "Aria", 18);
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;