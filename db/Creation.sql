CREATE DATABASE who_funds_your_feed;

USE who_funds_your_feed;

CREATE TABLE Users (
	user_id int NOT NULL,
	user_name varchar(255),
	PRIMARY KEY (user_id)
);

CREATE TABLE Videos (
	video_id varchar(15) NOT NULL,
	title TINYTEXT,
	channel_name varchar(255) NOT NULL,
	video_category ENUM("Autos & Vehicles","Film & Animation","Music","Pets & Animals","Sports","Short Movies","Travel & Events","Gaming","Videoblogging","People & Blogs","Comedy","Entertainment","News & Politics","Howto & Style","Education","Science & Technology","Nonprofits & Activism","Movies","Anime/Animation","Action/Adventure","Classics","Comedy","Documentary","Drama","Family","Foreign","Horror","Sci-Fi/Fantasy") NOT NULL,
	video_duration_secs int NOT NULL,
	is_sponsored boolean NOT NULL,
	PRIMARY KEY (video_id)
);

CREATE TABLE Brands (
	brand_id int NOT NULL AUTO_INCREMENT,
	brand_name varchar(255) NOT NULL,
	brand_rating int
	PRIMARY KEY brand_id
);

CREATE TABLE Watches (
	watch_id int NOT NULL AUTO_INCREMENT,
	user_id int,
	video_id varchar(15),
	time_watched TIMESTAMP,
	PRIMARY KEY (watch_id),
	FOREIGN KEY (user_id) REFERENCES Users(user_id),
	FOREIGN KEY (video_id) REFERENCES Videos(video_id)
);

CREATE TABLE Sponsorships (
	sponsorship_id int NOT NULL AUTO_INCREMENT,
	brand_id int,
	video_id varchar(15),
	PRIMARY KEY (watch_id),
	FOREIGN KEY (brand_id) REFERENCES Brands(brand_id),
	FOREIGN KEY (video_id) REFERENCES Videos(video_id)
);