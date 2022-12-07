const $ = window.$;

$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  data.results.forEach(movie => {
    $('UL#list_movies').append(`<li>${movie.title}</li>`);
  });
});
