$(function () {
  $('div#add_item').on('click', () => {
    const list = document.createElement('li');
    list.innerHTML = 'Item';
    $('ul.my_list').append(list);
  });
});
