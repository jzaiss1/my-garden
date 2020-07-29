/********************************************************
* This script creates the database named mygarden
*********************************************************/
DROP DATABASE IF EXISTS mygarden;
CREATE DATABASE mygarden;
USE mygarden;

-- create the tables for the database
CREATE TABLE Tags 
(
	TagID		INT					PRIMARY KEY	AUTO_INCREMENT,
	Tag			VARCHAR(45) NOT NULL
);

CREATE TABLE Status_tbl 
(
	StatusID			INT					 PRIMARY KEY	AUTO_INCREMENT,
	Status_Name		VARCHAR(45)  NOT NULL
);

CREATE TABLE Photo_tags
(
	Photo_tagID		INT				PRIMARY KEY		AUTO_INCREMENT,
	tagID					INT				NULL					REFERENCES Tags (TagID),
	photoID				INT				NULL					REFERENCES Photos (PhotoID),
	INDEX 				tagID_idx 	(tagID ASC),
	INDEX 				photoID_idx (photoID ASC)
);

CREATE TABLE Photos
(
	PhotoID				INT						PRIMARY KEY	AUTO_INCREMENT,
	image_blob		BLOB,
	image_date		DATE,
	plantID				INT						NULL		REFERENCES Plants (PlantID),
	comments 			VARCHAR(256),
	INDEX 				plantID_idx 			(plantID ASC)
);

CREATE TABLE Plants
(
	PlantID				INT						PRIMARY KEY AUTO_INCREMENT,
	plantName			VARCHAR(45)		NOT NULL,
	watering			VARCHAR(100),
	hardiness			VARCHAR(100),
	fertilization VARCHAR(100),
	totalSize			VARCHAR(100),
	spacing				VARCHAR(100),
	details				VARCHAR(100),
	blooms				VARCHAR(100),
	zones					VARCHAR(45),
	statusID			INT						NULL		REFERENCES Status_tbl (StatusID),
	INDEX 				statusID_idx 	(statusID ASC)
);