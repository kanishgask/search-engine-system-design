CREATE TABLE documents (

doc_id INT PRIMARY KEY,
url TEXT,
content TEXT

);

CREATE TABLE index_table (

word VARCHAR(100),
doc_id INT

);
