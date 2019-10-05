// AIM : Ensure that foreground and background color combinations provide sufficient contrast
// so that for any give value og background, we set the text color 
// to something that is clearly visible.

// here a div(or any html selector for that matter) has class bg.

var rgb = [255, 0, 0];

// randomly change to showcase updates
setInterval(setContrast, 1000);

function setContrast() {
  // randomly update
  rgb[0] = Math.round(Math.random() * 255);
  rgb[1] = Math.round(Math.random() * 255);
  rgb[2] = Math.round(Math.random() * 255);

  // ALGORITHM HERE : http://www.w3.org/TR/AERT#color-contrast
  var o = Math.round(((parseInt(rgb[0]) * 299) +
                      (parseInt(rgb[1]) * 587) +
                      (parseInt(rgb[2]) * 114)) / 1000);
  
  // calculate bg and fg
  var fore = (o > 125) ? 'black' : 'white';
  var back = 'rgb(' + rgb[0] + ',' + rgb[1] + ',' + rgb[2] + ')';
  
  // apply to DOM
  $('#bg').css('color', fore); 
  $('#bg').css('background-color', back);
  
}