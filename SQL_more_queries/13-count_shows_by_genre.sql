-- Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT tv_genres.name, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genres_id
GROUP BY tv_genres.id
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY number_of_shows DESC;