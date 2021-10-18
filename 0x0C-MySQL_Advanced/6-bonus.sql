-- Add bonus 
DELIMITER $$

CREATE PROCEDURE AddBonus(
    IN user_id INT ,
    project_name VARCHAR(255),
    score FLOAT
)
BEGIN
    INSERT INTO projects (name)
    SELECT project_name FROM DUAL
    WHERE NOT EXISTS (SELECT * FROM projects WHERE name = project_name);
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END$$
DELIMITER;
