const Paddle = function (player, color){
	
	const c = color
	const w = 30
	const h = 200
	const p = player  
					// ? es un if corto   : en caso constrario
	const x = p === 1 ? 0 : width - w 
	const speed = 20
	const UP = -1
	const DOWN = 1
	let y = Math.floor(height / 2)
	let score = 0

	const getX = function(){
		return x
	}
	const getY = function(){
		return y
	}

	const getW = function(){
		return w
	}

	const getH = function(){
		return h
	}
	const getScore = function(){
		return score
	}


	const draw = function (){
		rectMode(CORNER)
		noStroke()
		fill(c)
		rect(x, y, w, h)
		
	}

	const move = function(dir){
		if(edge(dir))
		y += (speed * dir)
	}

	const edge = function(dir){
		return(dir === UP && y > 0 || dir === DOWN && y < height - h)

	}

	const updateScore = function(){
		score++
	}

	return{
		draw,
		move,
		getH,
		getW,
		getX,
		getY,
		getScore,
		updateScore
	}

}