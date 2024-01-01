function copyDivToClipboard(event) {
  var div = event.target.parentNode.parentNode
  console.log(div)
  var range = document.createRange();

  range.selectNode(div);
  window.getSelection().removeAllRanges(); 
  window.getSelection().addRange(range); 
  document.execCommand("copy");
  window.getSelection().removeAllRanges();
  alert(`text copied ${div.firstElementChild.nextSibling.nodeValue}`)
}

