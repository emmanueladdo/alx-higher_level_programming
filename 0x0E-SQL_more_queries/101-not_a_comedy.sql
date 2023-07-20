-- List all shows without genre 'Comedy' in 'hbtn_0d_tvshows'
-- 'tv_genres' table contains only one record where name = Comedy
-- Each record should display tv_shows.title
-- You can use max of 2 SELECT statements
SELECT title
FROM tv_shows
WHERE title NOT IN
(SELECT title
	FROM tv_shows
	LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
	LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
	WHERE tv_genres.name = 'Comedy')
GROUP BY title
ORDER BY title ASC;
