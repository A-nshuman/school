use school;
create table sinfo(roll int(4), name varchar(225), stream varchar(225));
alter table sinfo add address varchar(225);
alter table sinfo drop column address;
alter table sinfo modify column name varchar(30);
alter table sinfo add primary key (roll);
desc sinfo;
create table sinfo1(roll_no int(4) primary key, class int(2), foreign key (roll_no) references sinfo(roll));
desc sinfo1;
