
create table user(
    id integer not null primary key,
    phone varchar(255),
    name varchar(255),
    registered datetime,
    last_visit datetime
);

create table anime(
    id integer not null primary key,
    page integer,
    name_rus varchar(255),
    name_eng varchar(255),
    release_date datetime,
    description varchar(255),
    alternative_description varchar(255),
    rating float,
    picture_path varchar(255), --путь к файлу на сервере
);

create table genre(
    id integer not null primary key,
    name_rus varchar(255),
    name_eng varchar(255)
);

create table studio(
    id integer not null primary key,
    name varchar(255)
);


create table anime_genre(
    anime_id integer not null,
    genre_id integer not null,
    FOREIGN KEY(anime_id) REFERENCES anime(id),
    FOREIGN KEY(genre_id) REFERENCES genre(id)
);

create table anime_studio(
    studio_id integer not null,
    anime_id integer not null,
    FOREIGN KEY(anime_id) REFERENCES anime(id),
    FOREIGN KEY(studio_id) REFERENCES studio(id)
);

create table anime_name(
    anime_id integer not null,
    name varchar(255),
    FOREIGN KEY(anime_id) REFERENCES anime(id),
);

create table assessment(
    id integer not null primary key,
    user_id integer not null,
    anime_id integer not null,
    score int not null, --предположительные значения: -1, 0, 1
    FOREIGN KEY(user_id) REFERENCES user(id),
    FOREIGN KEY(anime_id) REFERENCES anime(id)
);

create table recommendation(
    id integer not null primary key,
    user_id integer not null,
    anime_id integer not null,
    score float not null,
    FOREIGN KEY(user_id) REFERENCES user(id),
    FOREIGN KEY(anime_id) REFERENCES anime(id)
);
