create table users(
    id serial primary key,
    username varchar(64) not null,
    email varchar(64) not null
);

create table document(
    id serial primary key,
    title varchar(32) not null,
    contents varchar(64) not null,
    user_id int,
    constraint fk_user_document foreign key (user_id) references users(id)
);