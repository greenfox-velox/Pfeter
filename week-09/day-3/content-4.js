// replace the list items' content with items from this list:
// ['apple', 'banana', 'cat', 'dog']
var itemsList = ['apple', 'banana', 'cat', 'dog'];
var allLi = document.querySelectorAll('li');
for (let i = 0; i < allLi.length; i++) {
  allLi[i].textContent = itemsList[i];
}
