// target all path elements describing the gusts of air around the race car
const paths = document.querySelectorAll('path.air');

/*
for each path update the --stroke-dash property to match the length of the stroke
! create another property for the negative offset (mostly due to Edge not liking the calc() function with custom properties)
! include also an increasing delay to animate the path in sequence
*/
// add an increasing delay to the animation
paths.forEach((path, index) => {
  const totalLength = path.getTotalLength();
  path.style.setProperty('--stroke-dash', totalLength);
  path.style.setProperty('--stroke-dash-negative', -totalLength);
  // ! as the first path actually describes a stroke on the left side of the car, tailor its delay to occur with the dashes on the left side
  if (index === 0) {
    path.style.animationDelay = `${0.08 * (paths.length - 2)}s`;
  } else {
    path.style.animationDelay = `${0.08 * index}s`;
  }
});
var TxtType = function(el, toRotate, period) {
  this.toRotate = toRotate;
  this.el = el;
  this.loopNum = 0;
  this.period = parseInt(period, 10) || 2000;
  this.txt = '';
  this.tick();
  this.isDeleting = false;
};

TxtType.prototype.tick = function() {
  var i = this.loopNum % this.toRotate.length;
  var fullTxt = this.toRotate[i];

  if (this.isDeleting) {
  this.txt = fullTxt.substring(0, this.txt.length - 1);
  } else {
  this.txt = fullTxt.substring(0, this.txt.length + 1);
  }

  this.el.innerHTML = '<span class="wrap">'+this.txt+'</span>';

  var that = this;
  var delta = 200 - Math.random() * 100;

  if (this.isDeleting) { delta /= 2; }

  if (!this.isDeleting && this.txt === fullTxt) {
  delta = this.period;
  this.isDeleting = true;
  } else if (this.isDeleting && this.txt === '') {
  this.isDeleting = false;
  this.loopNum++;
  delta = 500;
  }

  setTimeout(function() {
  that.tick();
  }, delta);
};

window.onload = function() {
  var elements = document.getElementsByClassName('typewrite');
  for (var i=0; i<elements.length; i++) {
      var toRotate = elements[i].getAttribute('data-type');
      var period = elements[i].getAttribute('data-period');
      if (toRotate) {
        new TxtType(elements[i], JSON.parse(toRotate), period);
      }
  }
  // INJECT CSS
  var css = document.createElement("style");
  css.type = "text/css";
  css.innerHTML = ".typewrite > .wrap { border-right: 0.08em solid #fff}";
  document.body.appendChild(css);
};