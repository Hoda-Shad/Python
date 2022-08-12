INSERT INTO custumers
VALUES(1,'shad','mashad','iran');
INSERT INTO custumers
VALUES(2,'alipur','mashad','iran');
INSERT INTO custumers
VALUES(3,'ganji','shahr rei','iran');
INSERT INTO custumers
VALUES(4,'yosefi','mashad','iran');
INSERT INTO custumers
VALUES(5,'samadi','edmonton','canada');

SELECT * FROM products WHERE count!=0;

DELETE FROM custumers WHERE country != 'iran';


INSERT INTO products 
VALUES(001, 'glue', 1000, 380);

INSERT INTO Products 
VALUES(002, 'cable', 55000, 610);

UPDATE products
SET price = price*0.8
WHERE count!=0;
