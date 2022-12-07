const $ = window.$;

$('div#toggle_header').click(function () {
  $('header').toggleClass('red').toggleClass('green');
});
