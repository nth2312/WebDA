create database dtb_web;
use dtb_web;

create table tbl_user(
	user_username varchar(10) primary key,
    user_password varchar(12),
    user_email varchar(40)
);

create table tbl_hotel(
	hotel_id int primary key,
    hotel_name varchar(25),
    hotel_address varchar(25),
    average_price int
);

create table tbl_place(
	place_id int primary key,
    place_name varchar(25),
    place_address varchar(25),
    entry_price int
);

create table tbl_admin(
	admin_username varchar(10) primary key,
    admin_password varchar(12)
);

create table tbl_hotel_review(
	id int primary key,
    user_username varchar(10),
    hotel_id int,
    review_like int,
    review_dislike int,
    review_comment varchar(100),
    foreign key (user_username) references tbl_user(user_username),
    foreign key (hotel_id) references tbl_hotel(hotel_id)
);

create table tbl_place_review(
	id int primary key,
    user_username varchar(10),
    place_id int,
    review_like int,
    review_dislike int,
    review_comment varchar(100),
    foreign key (user_username) references tbl_user(user_username),
    foreign key (place_id) references tbl_place(place_id)
);

create table tbl_user_feedback(
	id int primary key,
    fb_type varchar(10),
    fb_detail varchar(25),
    user_username varchar(10),
    foreign key (user_username) references tbl_user(user_username)
);

insert into tbl_user values("khanhhue", "Khanhhue16112002@", "yangyihye2002@gmail.com");