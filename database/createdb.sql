
--code from previous project
create table category(
    codename varchar(255) primary key,
    name varchar(255),
    aliases text
);

create table record(
    id integer primary key,
    created datetime,
    time_count integer,
    category_codename integer,
    raw_text text,
    FOREIGN KEY(category_name) REFERENCES category(codename)
);
