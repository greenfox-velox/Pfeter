// fill output1 with the first paragraph's content, text only.
var contentOfTheFirstParagraph = document.querySelector('p');
var output1 = document.querySelector('.output1');
output1.innerHTML = contentOfTheFirstParagraph.textContent;

// fill output2 with the first paragraph's content keeping the cat strong.
var output2 = document.querySelector('.output2');
output2.innerHTML = contentOfTheFirstParagraph.innerHTML;
