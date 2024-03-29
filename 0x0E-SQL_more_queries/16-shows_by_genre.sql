-- List all shows and genres linked to show from 'hbtn_0d_tvshows'
-- If show doesn't have a genre, display NULL in genre column
-- Each record should display tv_shows.title, tv_genres.name
-- Results must be sorted in ascending order by show title
SELECT title, name
FROM tv_shows
LEFT JOIN tv_show_genres s ON tv_shows.id = s.show_id
LEFT JOIN tv_genres g ON s.genre_id = g.id
ORDER BY title ASC, name ASC;
