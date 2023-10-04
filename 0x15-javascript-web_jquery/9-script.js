/* JavaScript script cript that
updates the text of the <header> element to New Header
ou must use the JQuery API
*/
$('document').ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
  });
});
