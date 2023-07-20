-- List all Comedy shows in 'hbtn_0d_tvshows'
-- 'tv_genres' table contains only one record where name = Comedy
-- Results must be sorted in ascending order by the show title
SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres tv ON tv_shows.id = tv.show_id
INNER JOIN tv_genres gn ON tv.genre_id = tv.id
WHERE gn.name = 'Comedy'
ORDER BY tv_shows.title ASC;
