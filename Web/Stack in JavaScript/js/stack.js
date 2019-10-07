class Stack {
  constructor() {
    this.count = -1;
    this.data = {};
  }

  push(val){
    this.data[++this.count] = val;
  }

  pop(){
    if (this.count === -1) {
      window.alert('Stack Underflow!');
      return undefined;
    } else {
      var val = this.data[this.count];
      this.count--;
      delete this.data[val];
      return val;
    }
  }

  disp(){
    var S;
    if (this.count === -1) {
      S = "";
    } else {
      var S = "";
      for (var i = this.count; i >= 0; i--) {
        if(i == this.count)
          S += "  <font size='6px'>" + this.data[i] + "</font>";
        else
          S += "<br />  <font size='6px'>" + this.data[i] + "</font>";
      }
    }
    document.getElementById('stackElements').innerHTML = S;
    document.getElementById('stackElements').style.color = 'teal';
  }

}

const s = new Stack();

function pushIt(){
  var x = parseInt(prompt('Enter the value: '));
  s.push(x);
  s.disp();
}

function popIt(){
  var popped = s.pop();
  if(popped !== undefined)
    window.alert('Popped: ' + popped);
  s.disp();
}
