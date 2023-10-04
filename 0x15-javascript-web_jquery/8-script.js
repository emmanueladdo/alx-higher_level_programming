/* JavaScript script cript that
updates the text of the <header> element to New Header
ou must use the JQuery API
*/
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
});
