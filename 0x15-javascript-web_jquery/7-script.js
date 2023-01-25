$(function () {
  $.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json',
    (res) => {
      $('div#character').text(res.name);
    });
});
