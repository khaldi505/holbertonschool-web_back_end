-- creating a trigger, that triggers ?? when a new order inserted

CREATE TRIGGER decreasse_quantity
AFTER INSERT ON orders
FOR EACH ROW UPDATE items
SET quantity = quantity - NEW.number
WHERE items.name = NEW.item_name;
