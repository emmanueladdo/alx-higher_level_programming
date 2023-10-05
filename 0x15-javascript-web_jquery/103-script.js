$(document).ready(function () {
  // Define the base URL for the API
  const url = 'https://www.fourtonfish.com/hellosalut/?';

  // Add a click event handler to the button with id 'btn_translate'
  $('INPUT#btn_translate').click(function () {
    // Fetch the language code entered by the user from the input field
    const languageCode = $('INPUT#language_code').val();

    // Make a GET request to the API with the language code as a parameter
    $.get(url + $.param({ lang: languageCode }), function (data) {
      // Update the content of the DIV#hello with the translation
      $('DIV#hello').html(data.hello);
    });
  });
});

