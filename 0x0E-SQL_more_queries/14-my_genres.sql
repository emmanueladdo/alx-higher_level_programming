-- 'hbtn_0d_tvshows' to list all genres of show 'Dexter'
-- 'tv_shows' table contains only one record where title = Dexter
-- Each record should display tv_genres.name
-- Results must be sorted in ascending order by genre name
-- You can only use one SELECT statement
SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres b ON tv_genres.id = b.genre_id
INNER JOIN tv_shows sh ON b.show_id = sh.id
WHERE sh.title = 'Dexter'
ORDER BY tv_genres.name ASC;
