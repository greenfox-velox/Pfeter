// 1. Alert the content of the heading.
var contentOfTheHeading = document.querySelector('h1');
console.log(contentOfTheHeading.innerHTML);
// 2. Write the content of the first paragraph to the console.
var contentOfTheFirstParagraph = document.querySelector('p');
console.log(contentOfTheFirstParagraph.innerHTML);
// 3. Alert the content of the second paragraph.
var contentOfTheParagraphs = document.querySelectorAll('p');
console.log(contentOfTheParagraphs[1].innerHTML);
// 4. Replace the heading's content with 'New content'.
var contentOfTheHeading = document.querySelector('h1');
contentOfTheHeading.innerHTML = 'New content';
// 5. Replace the last paragraph's content with the first paragraph's content.
var contentOfTheParagraphs = document.querySelectorAll('p');
contentOfTheParagraphs[contentOfTheParagraphs.length - 1].innerHTML = contentOfTheParagraphs[0].innerHTML;
