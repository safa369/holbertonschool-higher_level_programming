-- count shows by genre.
SELECT tg.name AS genre,
COUNT(*) AS number_of_shows
FROM tv_genres AS tg
JOIN tv_show_genres AS tsg 
ON tg.id=tsg.genre_id
GROUP BY tg.name
ORDER BY number_of_shows DESC;