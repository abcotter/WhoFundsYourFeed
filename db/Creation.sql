CREATE DATABASE who_funds_your_feed;

USE who_funds_your_feed;

CREATE TABLE who_funds_your_feed.Users (
	user_id VARCHAR(255) NOT NULL,
	user_name varchar(255),
	PRIMARY KEY (user_id)
);

INSERT INTO who_funds_your_feed.Users(user_id, user_name) VALUES ('10001', 'testUser');
INSERT INTO who_funds_your_feed.Users(user_id, user_name) VALUES ('10002', 'FatimahAreola');
INSERT INTO who_funds_your_feed.Users(user_id, user_name) VALUES ('10003', 'CarlaLeal');
INSERT INTO who_funds_your_feed.Users(user_id, user_name) VALUES ('10004', 'AbiCotter');
INSERT INTO who_funds_your_feed.Users(user_id, user_name) VALUES ('10005', 'NayabButt');
INSERT INTO who_funds_your_feed.Users(user_id, user_name) VALUES ('10006', 'MoQaderi');

CREATE TABLE who_funds_your_feed.Channels (
	channel_id varchar(255) NOT NULL,
	channel_name varchar(255) NOT NULL,
	channel_location varchar(50) NOT NULL,
	channel_thumbnail varchar(255), 
	video_count int NOT NULL, 
	sub_count varchar(50) NOT NULL,
	PRIMARY KEY (channel_id)
);

INSERT INTO who_funds_your_feed.Channels (channel_id, channel_name, channel_location, channel_thumbnail, video_count, sub_count) Values ("{channelId}", "TheSorryGirls", "Canada", "yikesnourl", 300, "2110000");

CREATE TABLE who_funds_your_feed.Videos (
	video_id varchar(15) NOT NULL,
	title TINYTEXT,
	channel_id varchar(255) NOT NULL,
	video_category ENUM("Autos & Vehicles","Film & Animation","Music","Pets & Animals","Sports","Short Movies","Travel & Events","Gaming","Videoblogging","People & Blogs","Comedy","Entertainment","News & Politics","Howto & Style","Education","Science & Technology","Nonprofits & Activism","Movies","Anime/Animation","Action/Adventure","Classics","Comedy","Documentary","Drama","Family","Foreign","Horror","Sci-Fi/Fantasy") NOT NULL,
	video_duration_secs int NOT NULL,
	is_sponsored boolean NOT NULL,
	PRIMARY KEY (video_id)
	FOREIGN KEY (channel_id) REFERENCES Channels(channel_id)
);

INSERT INTO who_funds_your_feed.Videos (video_id, title, channel_name, video_category, video_duration_secs, is_sponsored) VALUES ('VE3Vej963UE', 'sharing my EASY space saving and dorm friendly DIYs', 'TheSorryGirls', 'Howto & Style', '897', '1');


CREATE TABLE who_funds_your_feed.Brands (
	brand_name varchar(255) NOT NULL,
	brand_url TINYTEXT,
	PRIMARY KEY (brand_name)
);

INSERT INTO who_funds_your_feed.Brands (brand_name, brand_url) VALUES ('Native', 'https://www.nativecos.com/');

CREATE TABLE who_funds_your_feed.Watches (
	user_id VARCHAR(255),
	video_id varchar(15),
	time_watched TIMESTAMP,
	PRIMARY KEY (user_id,video_id, time_watched),
	FOREIGN KEY (user_id) REFERENCES Users(user_id),
	FOREIGN KEY (video_id) REFERENCES Videos(video_id)
);

INSERT INTO who_funds_your_feed.Watches(user_id, video_id, time_watched) VALUES ('aaaaaaaa-bbbb-bbbb-bbbb-aaaaaaaa','VE3Vej963UE', '2022-01-11 00:00:00');

CREATE TABLE who_funds_your_feed.Sponsorships (
	brand_name varchar(255),
	video_id varchar(15),
	PRIMARY KEY (brand_name, video_id),
	FOREIGN KEY (brand_name) REFERENCES Brands(brand_name),
	FOREIGN KEY (video_id) REFERENCES Videos(video_id)
);

INSERT INTO who_funds_your_feed.Sponsorships (brand_name, video_id) VALUES ('Native', 'VE3Vej963UE');
