CREATE TABLE account (
	id INTEGER NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	"messageCount" INTEGER, 
	admin BOOLEAN NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (admin IN (0, 1))
);

CREATE TABLE group (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE area (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	"messageCount" INTEGER, 
	PRIMARY KEY (id)
);

CREATE TABLE groupuser (
	id INTEGER NOT NULL, 
	user_id INTEGER NOT NULL, 
	group_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES account (id), 
	FOREIGN KEY(group_id) REFERENCES "group" (id)
);

CREATE TABLE post (
	id INTEGER NOT NULL, 
	title VARCHAR(144) NOT NULL, 
	content VARCHAR(144) NOT NULL, 
	"createdOn" DATETIME, 
	"messageCount" INTEGER, 
	user_id INTEGER NOT NULL, 
	area_id INTEGER, 
	group_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES account (id), 
	FOREIGN KEY(area_id) REFERENCES area (id), 
	FOREIGN KEY(group_id) REFERENCES "group" (id)
);

CREATE TABLE answer (
	id INTEGER NOT NULL, 
	content VARCHAR(144) NOT NULL, 
	"createdOn" DATETIME, 
	user_id INTEGER NOT NULL, 
	post_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES account (id), 
	FOREIGN KEY(post_id) REFERENCES post (id)
);

