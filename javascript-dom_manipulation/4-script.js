document.querySelector('#add_item').addEventListener('click', function () {
  const my_list = document.querySelector('.my_list');
  const li = document.createElement('li');
  li.textContent = 'Item';
  my_list.append(li);
});
