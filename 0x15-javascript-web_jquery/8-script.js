$(function () {
  $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json',
    (res) => {
      for (const array of res.results) {
        const list = document.createElement('li');
        list.innerHTML = array.title;
        $('ul#list_movies').append(list);
      }
    });
});
