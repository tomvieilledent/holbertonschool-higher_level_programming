fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(res => res.json())
  .then(data => {
    const list = document.getElementById('list_movies');
    data.results.forEach(movies => {
      const li = document.createElement('li');
      li.textContent = movies.title;
      list.appendChild(li);
    })
  })
  .catch(error => console.error('Error', error));