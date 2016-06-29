// Does cat have a cat class?
// If so, alert 'YEAH CAT!'
// If dolphin has a 'dolphin' class, replace apple's content with 'pear'
// If apple has an 'apple' class, replace cat's content with 'dog'
// Make apple red
// Make balloon less balloon-like

const pList = document.querySelectorAll('p');
for (let i = 0; i < pList.length; i++) {
  if (pList[i].textContent === 'cat' && pList[i].classList.contains('cat')) {
    alert('YEAH CAT');
  }
  if (pList[i].textContent === 'dolphin' && pList[i].classList.contains('dolphin')) {
    for (let j = 0; j < pList.length; j++) {
      if (pList[j].textContent === 'apple') {
        pList[j].textContent = 'pear';
      }
    }
  }
  if (pList[i].textContent === 'apple' && pList[i].classList.contains('apple')) {
    for (let k = 0; k < pList.length; k++) {
      if (pList[k].textContent === 'cat') {
        pList[k].textContent = 'dog';
      }
    }
  }
  document.querySelector('.apple').classList.add('red');
  document.querySelector('.balloon').classList.remove('balloon');
}
