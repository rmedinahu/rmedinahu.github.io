
create table makes(
pk int not null, 
make varchar(24),
primary key (pk)
);

create table cars(
pk int not null, 
make int not null, 
year int, 
odom int, 
primary key (pk),
foreign key (make) references makes (pk)
);



