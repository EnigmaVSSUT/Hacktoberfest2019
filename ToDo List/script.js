var input = document.getElementById("userinput");
var button = document.getElementById("enter");
var ul = document.querySelector("ul");
var listItems = document.getElementsByTagName("li");

function inputLength() {
	return input.value.length;
}


function createListElement(){
	var li = document.createElement("li");
	li.appendChild(document.createTextNode(input.value));
	ul.appendChild(li);
	input.value = "";

	addDoneAfterClick();

	var btnDelete = document.createElement("button");
	btnDelete.appendChild(document.createTextNode("X"));
    li.appendChild(btnDelete);
    btnDelete.addEventListener("click", addDeleteBtn);
}

function addListAfterClick(){
	if (inputLength() > 0) {
		createListElement();
	}
}

function addListAfterKeypress(event){
	if (inputLength() > 0 && event.keyCode === 13) {
		createListElement();
	}
}

function addToggleDone(){
	this.classList.toggle("done");
}

function addDoneAfterClick() {
	for (var i=0; i < listItems.length; i++) {
		listItems[i].addEventListener("click", addToggleDone);
	}
}

addDoneAfterClick();

function addDeleteBtn() {
	ul.removeChild(this.parentElement);
}

function addDeleteAfterClick() {
	for(var i=0; i < listItems.length; i++){
		var btnDelete = document.createElement("button");
    	listItems[i].appendChild(btnDelete);
		btnDelete.appendChild(document.createTextNode("X"));
		btnDelete.addEventListener("click", addDeleteBtn);
	}
}

addDeleteAfterClick();

button.addEventListener("click", addListAfterClick);
input.addEventListener("keypress", addListAfterKeypress);


