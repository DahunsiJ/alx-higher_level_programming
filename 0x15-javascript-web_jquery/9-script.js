$(function () {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr',
    (res) => {
      console.log(res);
      $('div#hello').append(res.hello);
    });
});
