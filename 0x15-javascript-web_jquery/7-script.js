/* JavaScript script cript that
updates the text of the <header> element to New Header
ou must use the JQuery API
*/
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('DIV#character').text(data.name);
});
