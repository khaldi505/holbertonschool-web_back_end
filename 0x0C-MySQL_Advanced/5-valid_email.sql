-- rests valid_email when email changed
DELIMITER $$
DROP TRIGGER IF EXISTS rest_valid_email;
CREATE TRIGGER rest_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
IF NEW.email <> OLD.email
THEN SET NEW.valid_email = 0;
END IF;
END $$
