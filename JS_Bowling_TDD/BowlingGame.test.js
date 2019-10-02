const { expect } = require("chai");
const Game = require("./BowlingGame");

var game;

const rollMany = (pins, n) => {
  for (let i = 0; i < n; i++) {
    game.roll(pins);
  }
};

const rollSpare = () => {
  game.roll(5);
  game.roll(5);
};

const rollStrike = () => {
  game.roll(10);
};

describe("BowlingGame", () => {
  beforeEach(() => {
    game = new Game();
  });

  describe("gutter game", () => {
    it("should have score of 0", () => {
      rollMany(0, 20);
      expect(game.score()).to.equal(0);
    });
  });

  describe("an all 1's game", () => {
    it("should have score of 20", () => {
      rollMany(1, 20);
      expect(game.score()).to.equal(20);
    });
  });
  describe("a game with one spare", () => {
    it("should have higher multiplier", () => {
      rollSpare();
      game.roll(3);
      rollMany(0, 17);
      expect(game.score()).to.equal(16);
    });
  });
  describe("a game with one strike", () => {
    it("should have higher multiplier", () => {
      rollStrike();
      game.roll(3);
      game.roll(4);
      rollMany(0, 16);
      expect(game.score()).to.equal(24);
    });
  });
  describe("a perfect game", () => {
    it("should yield a score of 300", () => {
      rollMany(10, 12);
      expect(game.score()).to.equal(300);
    });
  });
});
