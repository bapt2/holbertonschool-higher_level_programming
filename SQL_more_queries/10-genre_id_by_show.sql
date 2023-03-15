-- inport the database dump from hbtn_0d_tvshows to your mysql server
SELECT tv_shows.title, tv_shows_genre.genre_id
FROM tv_shows, tv_shows_genre
WHERE tv_shows.id = tv_shows_genre.show_id
ORDER BY tv_shows.title ASC, tv_shows_genre.genre_id;