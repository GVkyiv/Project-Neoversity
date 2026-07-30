const categoriesList = document.querySelector('#categories');
const categoriesItems = categoriesList.querySelectorAll('.item');

console.log(`Number of categories: ${categoriesItems.length}`);

categoriesItems.forEach(category => {
  const title = category.querySelector('h2');
  const elements = category.querySelectorAll('ul li');

  console.log(`Category: ${title.textContent}`);
  console.log(`Elements: ${elements.length}`);
});
