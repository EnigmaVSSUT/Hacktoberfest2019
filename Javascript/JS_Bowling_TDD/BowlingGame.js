class Game {
  constructor() {
    this.rolls = new Array(21);
    this.currentRoll = 0;
  }
  roll(pins) {
    this.rolls[this.currentRoll++] = pins;
  }
  score() {
    let score = 0;
    let frameIndex = 0;
    for (let frame = 0; frame < 10; frame++) {
      if (this.isStrike(frameIndex)) {
        score += 10 + this.strikeBonus(frameIndex);
        frameIndex++;
      } else if (this.isSpare(frameIndex)) {
        score += 10 + this.spareBonus(frameIndex);
        frameIndex += 2;
      } else {
        score += this.sumInFrame(frameIndex);
        frameIndex += 2;
      }
    }
    return score;
  }

  isSpare(frameIndex) {
    return this.rolls[frameIndex] + this.rolls[frameIndex + 1] === 10;
  }
  isStrike(frameIndex) {
    return this.rolls[frameIndex] === 10;
  }
  strikeBonus(frameIndex) {
    return this.rolls[frameIndex + 1] + this.rolls[frameIndex + 2];
  }
  spareBonus(frameIndex) {
    return this.rolls[frameIndex + 2];
  }
  sumInFrame(frameIndex) {
    return this.rolls[frameIndex] + this.rolls[frameIndex + 1];
  }
}

module.exports = Game;
