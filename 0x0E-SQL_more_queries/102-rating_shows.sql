-- This script lists all shows from hbtn_0d_tvshows_rate by their rating.
--- Each record should display: tv_shows.title - rating sum
--- Results must be sorted in descending order by the rating
--- You can use only one SELECT statement
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
