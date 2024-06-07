#User data
insert into tbl_user values("admin", "admin", "admin@gmail.com", 1);

#Place data
insert into tbl_place values(1, "Bảo tàng lịch sử Quốc gia", "216 Trần Quang Khải, Tràng Tiền", 40000, 21.02461539727238, 105.85977239563464);
insert into tbl_place values(2, "Hồ Gươm", "Hồ Hoàn Kiếm, Hàng Trống", 0, 21.02890491644988, 105.85219303426125); 
insert into tbl_place values(3, "Tràng Tiền Plaza", "24b Hai Bà Trưng, Tràng Tiền", 0, 21.024876868000593, 105.85315584960455);
insert into tbl_place values(4, "Nhà tù Hỏa Lò", "1 Hỏa Lò, Trần Hưng Đạo", 50000, 21.0253296806232, 105.84653173981394);
insert into tbl_place values(5, "Cầu Thê Húc", "Hồ Hoàn Kiếm, Hàng Trống", 0, 21.030821193932, 105.85281569563485);
insert into tbl_place values(6, "Nhà hát múa rối Thăng Long", "57b Đinh Tiên Hoàng, Hàng Bạc", 150000, 21.03192291890948, 105.85326076494813);
insert into tbl_place values(7, "Phố sách Hà Nội", "19 tháng 12, Trần Hưng Đạo", 0, 21.02525911510973, 105.84788260912715);
insert into tbl_place values(8, "Vườn hoa Lý Thái Tổ", "12 Lê Lai, Lý Thái Tổ", 0, 21.027645582640996, 105.85474871097819);
insert into tbl_place values(9, "Con đường gốm sứ", "12 Hàng Vôi, Lý Thái Tổ", 0, 21.030277064713818, 105.85740172261967);
insert into tbl_place values(10, "Phố Bích họa Phùng Hưng", "27b Phùng Hưng, Hàng Mã", 0, 21.03867190801747, 105.84694511097847);
insert into tbl_place values(11, "Nhà Thờ lớn Hà Nội", "40 Nhà Chung, Hàng Trống", 0, 21.028813795141076, 105.84887799563474);
insert into tbl_place values(12, "Đền Ngọc Sơn", "Hồ Hoàn Kiếm, Hàng Trống", 0, 21.03084910725805, 105.85245433981407);
insert into tbl_place values(13, "Chùa Quán Sứ", "73 Quán Sứ, Trần Hưng Đạo", 0, 21.02468365764751, 105.84538161097807);
insert into tbl_place values(14, "Tháp Bút", "Hồ Hoàn Kiếm, Hàng Trống", 0, 21.030855148984344, 105.8533911821424);
insert into tbl_place values(15, "Khu phố cổ Hà Nội", "Hàng Ngang, Hàng Đào", 0, 21.03443740515579, 105.85081186676028);
insert into tbl_place values(16, "Bốt Hàng Đậu", "Đồng Xuân, Quán Thánh", 0, 21.040512168582826, 105.84762542837362);
insert into tbl_place values(17, "Nhà hát Lớn Hà Nội", "1 Tràng Tiền, Phan Chu Trinh", 0, 21.02425521207461, 105.85798932632146);
insert into tbl_place values(18, "Phố đi bộ Hồ Gươm", "Gia Ngư, Phố cổ", 0, 21.025955199530063, 105.85323158029134);
insert into tbl_place values(19, "Bưu điện Hà Nội", "75b Đinh Tiên Hoàng, Tràng Tiền", 0, 21.02661847852201, 105.8537895649649);
insert into tbl_place values(20, "Tháp Hòa Phong", "75b Đinh Tiên Hoàng, Tràng Tiền", 0, 21.026377541011538, 105.85320842261967);

#Hotel data
insert into tbl_hotel values(1, "Silk Path Boutique", "21 Hàng Khay", 1500000);
insert into tbl_hotel values(2, "The La Sinfonia Majesty Hotel and Spa", "1 Cầu Gỗ", 1975000);
insert into tbl_hotel values(3, "May De Ville Legend Hotel and Spa", "23 Nguyên Siêu", 1060000);
insert into tbl_hotel values(4, "La Sinfonia Del Rey", "33-34 Hàng Dầu", 1900000);
insert into tbl_hotel values(5, "De L'Opera", "22 Tràng Tiền", 4724000);
insert into tbl_hotel values(6, "Mường Thanh Centre", "73 Thợ Nhuộm", 1100000);
insert into tbl_hotel values(7, "Melia Hotel", "44b Lý Thường Kiệt", 3275000);
insert into tbl_hotel values(8, "Sofitel Legend Metropole", "15 Ngô Quyền", 7520000);
insert into tbl_hotel values(9, "Mercure La Gare", "94 Lý Thường Kiệt", 1240000);
insert into tbl_hotel values(10, "Moon View 2", "61 Hàng Than", 1350000);

#Stores data
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (1, 'Xôi Xíu - Cơm Tấm Hà Nội', 'https://maps.app.goo.gl/5GytF17bZwhjugRr5');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (2, 'Hải sản phố 15A Trần Khánh Dư', 'https://maps.app.goo.gl/pK5jcD52Tqtk7fkm9');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (3, 'Quán cơm tấm Sài Gòn', 'https://maps.app.goo.gl/DfXoxPxh3A9s1tac7');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (4, 'Nhà hàng Luk Lak', 'https://maps.app.goo.gl/pPCh3ZE6FThazV1T8');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (5, 'Phở bò Nguyên Ký', 'https://maps.app.goo.gl/DfHmJmn2JxDUsSps5');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (6, 'Phở Thìn Bờ Hồ', 'https://maps.app.goo.gl/g5emWW8s3ngY8LP56');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (7, 'Lake View Side Restaurant', 'https://maps.app.goo.gl/JPr2BooECkS72GzR7');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (8, 'Phở Thủy Dương', 'https://maps.app.goo.gl/SNnjW574tbR7yZXTA');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (9, 'The Rhythms Restaurant', 'https://maps.app.goo.gl/kpEy5WLUGbHcVyTP7');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (10, 'J\'adore Café', 'https://maps.app.goo.gl/sXQ15U1AApCH2f7y5');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (11, 'Nem Nướng Nha Trang Quế Hoa', 'https://maps.app.goo.gl/AFfA8HzyqLQRkMtD8');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (12, 'Bánh mì phố', 'https://maps.app.goo.gl/467HMoQbpAM8UWRaA');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (13, 'Nhà hàng Quảng Đông Fu Rong Hua', 'https://maps.app.goo.gl/byoHCcvweMn6oPMc7');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (14, 'Nhà Hàng Thái Village', 'https://maps.app.goo.gl/byoHCcvweMn6oPMc7');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (15, 'Lục Thủy Restaurant & Lounge', 'https://maps.app.goo.gl/ixNRPPDnQVNs5e7s7');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (16, 'S\'Patisserie (Tràng Tiền Plaza)', 'https://maps.app.goo.gl/Sj95eFRHNJrY9EXM8');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (17, 'McDonald’s Hồ Gươm (Tràng Tiền Plaza)', 'https://maps.app.goo.gl/vszwgX97NRCH4f9m9');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (18, 'Bread factory - Tràng Tiền', 'https://maps.app.goo.gl/4895eXkhE93TxMLA7');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (19, 'Nhà Hàng Himalaya Restaurant', 'https://maps.app.goo.gl/mKTfHMYr7FCaNLF96');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (20, 'Le Thach Restaurant', 'https://maps.app.goo.gl/4mksftzvt1rRDJyD9');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (21, 'TEA EXPERT - Trà Nghệ Nhân', 'https://maps.app.goo.gl/pXxSJPA59WYsxXPR8');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (22, 'Le Beaulieu', 'https://maps.app.goo.gl/RVWYxG7ZKh9B8dz58');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (23, 'GoGi House Tràng Tiền', 'https://maps.app.goo.gl/cKr4kC9SwvhN5JuJ7');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (24, 'Kichi-Kichi Tràng Tiền', 'https://maps.app.goo.gl/jqMRw14usB3EnksU7');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (25, 'Nhà hàng Mỹ Tường Viên', 'https://maps.app.goo.gl/WeDK2hSEuvouJaYM8');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (26, 'Nhà Hàng San Hô Hà Nội', 'https://maps.app.goo.gl/dgtePsVjTUXzp5Pq9');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (27, 'Nhà Hàng Classico', 'https://maps.app.goo.gl/zNsQbX9V2yQhks8U9');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (28, 'Mỹ Vị Restaurant & Cafe', 'https://maps.app.goo.gl/jw11XGJqhdLgtraJ7');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (29, 'Nhà Hàng Song Phố', 'https://maps.app.goo.gl/AuWYWdkeWZbvWHPx5');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (30, 'Nhà Hàng Nhật Bản Kimono', 'https://maps.app.goo.gl/VwWNREVwVA15Xkyq5');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (31, 'Jaspas', 'https://maps.app.goo.gl/bgZ8hXjiBUXeMuEj8');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (32, 'Phở Thắng', 'https://maps.app.goo.gl/V9oFWsg2m6Vjz3236');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (33, 'Khu Ăn Vặt Trường Thpt Việt Đức', 'https://maps.app.goo.gl/yhFemCzu6kCmPSHP6');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (34, 'AHA Cafe', 'https://maps.app.goo.gl/dGvndtwauycbkVua6');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (35, 'cafe đơn - FLORIST & COFFEE', 'https://maps.app.goo.gl/d1Uu4B4RS9etPPZZ7');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (36, 'Panini & sandwiches', 'https://maps.app.goo.gl/8yiZRMEW1bZUeWtM6');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (37, 'Bay Seafood Buffet Hồ Gươm', 'https://maps.app.goo.gl/9Zx9Z3x9REnGdBpm8');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (38, 'Nhà Hàng Quỳnh Béo', 'https://maps.app.goo.gl/X2BsnNnSTzneycHo8');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (39, 'Cafe Rubi', 'https://maps.app.goo.gl/S3asSu5SwL6h5Q7PA');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (40, 'Quán Kem Tràng Tiền 8', 'https://maps.app.goo.gl/A2yygbC6fEGBXCkTA');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (41, 'Bún chả chị LAN', 'https://maps.app.goo.gl/cfkaXjXpDvGpMzoq5');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (42, 'Long Wang', 'https://maps.app.goo.gl/2kLhhatuxFkktxqGA');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (43, 'Nướng Xí Ngầu', 'https://maps.app.goo.gl/pxeSGJ27FRcYKAnQ6');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (44, 'Cơm Tấm 36', 'https://maps.app.goo.gl/xWepXpXYju8ax9pj7');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (45, 'Phở Lý Quốc Sư Phùng Hưng', 'https://maps.app.goo.gl/5tjHRr9cUTikzgTu6');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (46, 'Ếch Núp Lùm', 'https://maps.app.goo.gl/7PhsBKPGyyjqma4x9');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (47, 'Take Taco II', 'https://maps.app.goo.gl/FkD3YBZL8Y82iD5JA');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (48, 'Vivienne Café Restaurant', 'https://maps.app.goo.gl/coqb9vP15HP5WCz29');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (49, 'Nhà hàng La Place', 'https://maps.app.goo.gl/MEnanRbyJqqphyKc7');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (50, 'Godmother Hà Nội', 'https://maps.app.goo.gl/HCoHcxLjenvJ4cR87');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (51, 'Capos Hanoi - Spanish Tapas Bar', 'https://maps.app.goo.gl/tEDxpihPx5jT6RWe9');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (52, 'Kute Donuts Lý Thường Kiệt', 'https://maps.app.goo.gl/2o9N9dyroC461QwXA');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (53, 'Phở Chay Cô Hồng', 'https://maps.app.goo.gl/QxgGDYDmhCY91cdv9');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (54, 'HUSO Cuisine Express', 'https://maps.app.goo.gl/LhU5qBQ1sLBrkgGU7');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (55, 'CHILL 88 COFFEE', 'https://maps.app.goo.gl/QPVhagifpoS8zcPf7');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (56, 'Phở gánh', 'https://maps.app.goo.gl/A1kSEzvHLLC1Tz156');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (57, 'Phở gà cô Hường', 'https://maps.app.goo.gl/eeJpGCAUy812Vjpe8');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (58, 'Atithi Indian Vegetarian Hanoi', 'https://maps.app.goo.gl/qhin5LqLsDFMVcQ5A');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (59, 'Cái Mâm Restaurant', 'https://maps.app.goo.gl/eJYwvrjRe4prQpLr9');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (60, 'Bánh Mì ơi', 'https://maps.app.goo.gl/XJmWm1U7wm58evAw8');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (61, 'Bún Chả 31 Hàng Bồ', 'https://maps.app.goo.gl/P99RtJLhSUWe7csHA');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (62, 'Bi Don Don Cơm Cháy', 'https://maps.app.goo.gl/1chxkadtLf4S3Re17');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (63, 'Bánh Mì Như Hoa', 'https://maps.app.goo.gl/9xFYTeWPSgUu1eZZ9');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (64, 'Bánh cốm Hồng Ninh', 'https://maps.app.goo.gl/sknqzxDMapGs6GK47');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (65, 'Bò nướng Cúc Phương', 'https://maps.app.goo.gl/XzrmEcjLGugqoPay8');
INSERT INTO tbl_stores (store_id, store_name, link) VALUES (66, 'Bò Chất - Lẩu Nướng', 'https://maps.app.goo.gl/GpXt5gXRhE5VyZ9R6');

#Place_Stores
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (1, 1, 1);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (2, 1, 2);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (3, 1, 3);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (4, 1, 4);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (5, 1, 5);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (6, 5, 6);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (7, 5, 7);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (8, 5, 8);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (9, 5, 9);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (10, 5, 10);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (11, 5, 11);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (12, 5, 12);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (13, 12, 6);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (14, 12, 7);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (15, 12, 8);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (16, 12, 9);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (17, 12, 10);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (18, 12, 11);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (19, 12, 12);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (20, 14, 6);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (21, 14, 7);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (22, 14, 8);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (23, 14, 9);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (24, 14, 10);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (25, 14, 11);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (26, 14, 12);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (27, 2, 6);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (28, 2, 7);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (29, 2, 8);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (30, 2, 9);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (31, 2, 10);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (32, 2, 11);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (33, 2, 12);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (34, 2, 13);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (35, 2, 14);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (36, 2, 15);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (37, 2, 16);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (38, 2, 17);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (39, 2, 18);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (40, 6, 6);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (41, 6, 7);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (42, 6, 8);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (43, 6, 9);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (44, 6, 10);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (45, 6, 11);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (46, 6, 12);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (47, 8, 6);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (48, 8, 7);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (49, 8, 8);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (50, 8, 9);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (51, 8, 10);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (52, 8, 11);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (53, 8, 12);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (54, 18, 13);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (55, 18, 14);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (56, 18, 15);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (57, 18, 16);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (58, 18, 17);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (59, 18, 18);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (60, 19, 19);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (61, 19, 20);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (62, 19, 21);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (63, 19, 22);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (64, 20, 19);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (65, 20, 20);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (66, 20, 21);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (67, 20, 22);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (68, 3, 23);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (69, 3, 24);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (70, 3, 25);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (71, 4, 26);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (72, 4, 27);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (73, 4, 28);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (74, 4, 29);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (75, 4, 30);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (76, 4, 31);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (77, 7, 32);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (78, 7, 33);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (79, 7, 34);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (80, 7, 35);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (81, 7, 36);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (82, 8, 37);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (83, 8, 17);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (84, 8, 18);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (85, 9, 38);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (86, 9, 39);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (87, 9, 40);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (88, 9, 41);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (89, 10, 42);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (90, 10, 43);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (91, 10, 44);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (92, 10, 45);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (93, 10, 46);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (94, 11, 47);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (95, 11, 48);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (96, 11, 49);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (97, 11, 50);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (98, 11, 51);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (99, 13, 52);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (100, 13, 53);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (101, 13, 54);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (102, 13, 55);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (103, 15, 56);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (104, 15, 57);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (105, 15, 58);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (106, 15, 59);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (107, 15, 60);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (108, 15, 61);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (109, 16, 62);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (110, 16, 63);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (111, 16, 64);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (112, 16, 65);
INSERT INTO tbl_place_stores (id, place_id, store_id) VALUES (113, 16, 66);
