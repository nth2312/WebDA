create database dtb_web1;
use dtb_web1;

create table tbl_user(
	user_username varchar(10) primary key,
    user_password varchar(12),
    user_email varchar(40),
    user_role varchar(10)
);

create table tbl_hotel(
	hotel_id int primary key,
    hotel_name nvarchar(50),
    hotel_address nvarchar(50),
    average_price int
);

create table tbl_place(
	place_id int primary key,
    place_name nvarchar(50),
    place_address nvarchar(50),
    entry_price int,
    latitude varchar(20),
    longtitude varchar(20)
);

create table tbl_stores(
	store_id int primary key,
	store_name nvarchar(50),
    link varchar(100)
);

create table tbl_hotel_review(
	id int primary key,
    user_username varchar(10),
    hotel_id int,
    review_like int,
    review_dislike int,
    review_time date,
    review_comment nvarchar(100),
    foreign key (user_username) references tbl_user(user_username),
    foreign key (hotel_id) references tbl_hotel(hotel_id)
);

create table tbl_place_review(
	id int primary key,
    user_username varchar(10),
    place_id int,
    review_like int,
    review_dislike int,
    review_comment nvarchar(100),
    review_time date,
    foreign key (user_username) references tbl_user(user_username),
    foreign key (place_id) references tbl_place(place_id)
);

create table tbl_place_stores(
	id int primary key,
    place_id int,
    store_id int,
    foreign key (store_id) references tbl_stores(store_id),
    foreign key (place_id) references tbl_place(place_id)
);
