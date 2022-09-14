from data import data_manager
from psycopg2 import sql


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def actors_in_more_than_three_shows():
    return data_manager.execute_select("""SELECT actors.id, actors.name AS actor, actors.birthday AS bday
FROM actors
LEFT JOIN show_characters on actors.id = show_characters.actor_id
LEFT JOIN shows on show_characters.show_id = shows.id
GROUP BY actors.id
HAVING COUNT(DISTINCT shows.id) > 3
ORDER BY actors.birthday ASC
LIMIT 10;""")


def get_played_characters(current_actor):
    return data_manager.execute_select(sql.SQL('''
    SELECT actors.name, show_characters.character_name
    FROM actors
    LEFT JOIN show_characters on actors.id = show_characters.actor_id
    WHERE actors.name = {id};
    ''').format(id=sql.Literal(current_actor)))