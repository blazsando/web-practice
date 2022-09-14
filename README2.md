# Web practice project


## Tasks

1. select title, rating 2 decimals, year of release
    action shows
2. select title, number of seasons, number of characters
    shows higher than 8 rating

SELECT shows.title, count(DISTINCT s.season_number) as number_of_seasons, count(DISTINCT sc.character_name) as number_of_characters
FROM shows
LEFT JOIN seasons s on shows.id = s.show_id
LEFT JOIN show_characters sc on shows.id = sc.show_id
WHERE shows.rating > 8
GROUP BY shows.id
ORDER BY number_of_seasons DESC

3. select title, list genres, age of the movie
    more than 5 actors

SELECT  shows.title, STRING_AGG(g.name, ',') AS genre, extract(year from shows.year) AS show_year, a.name
FROM shows
LEFT JOIN  show_genres sg on shows.id = sg.show_id
LEFT JOIN genres g on g.id = sg.genre_id
LEFT JOIN show_characters sc on shows.id = sc.show_id
LEFT JOIN actors a on a.id = sc.actor_id
WHERE a.id > 5
GROUP BY shows.id, a.name

4. select title, name of characters, number of episodes
    odd number of episodes
5. select title, avg of actors birthyear, max age actor
    season special
6. select name, age of now or when died, number of shows
    character: himself, herself