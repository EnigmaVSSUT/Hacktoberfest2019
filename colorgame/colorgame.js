var colors =generateRandomColors(6);
var squares=document.querySelectorAll(".square");
var cp=pickColor();
var colordisplay=document.getElementById("colordisplay");
colordisplay.textContent=cp;
var message=document.querySelector("#message");
var header1 = document.querySelector("h1");
var header2= document.querySelector("h2");
for(var i=0;i<squares.length;i++)
{
	squares[i].style.backgroundColor=colors[i];
	squares[i].addEventListener("click",function(){
		var cc=this.style.backgroundColor;
		if(cc===cp)
		{
			message.textContent="Correct";
			
			changeColor(cp);
			header1.style.backgroundColor = cp;
			header2.style.backgroundColor = cp;
		}
		else
		{
			this.style.backgroundColor= "black";
			message.textContent="Try Again";
		}
	})
}
function changeColor(color)
{
	for(var i=0;i<squares.length;i++){
		squares[i].style.backgroundColor = color ;
	}
}
function pickColor(){
	var random=Math.floor(Math.random()*colors.length);
	return colors[random];
}
function generateRandomColors(num){
	var arr=[];
	for(var i=0 ; i<num;i++)
	{
			arr.push(randomColor());
	}
	return arr;
}
function randomColor()
{
	var r=Math.floor(Math.random()*256);
	var g=Math.floor(Math.random()*256);
	var b=Math.floor(Math.random()*256);
	return "rgb("+ r +", " + g + ", " + b +")";
}