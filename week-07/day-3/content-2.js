// fill every paragraph with the last one's content.
var contentOfTheParagraphs = document.querySelectorAll('p');
var lastContent = contentOfTheParagraphs[contentOfTheParagraphs.length - 1].innerHTML;
for (let i = 0; i < contentOfTheParagraphs.length - 1; i++) {
  contentOfTheParagraphs[i].innerHTML = lastContent;
}
