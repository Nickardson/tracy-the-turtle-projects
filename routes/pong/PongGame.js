const PongPlayer = require('./PongPlayer');
const PongBall = require('./PongBall');

module.exports = function () {
  this.home = new PongPlayer(true);
  this.away = new PongPlayer(false);

  this.ball = new PongBall();

  this.addPlayer = function (player) {
    if (player.home) {
      this.home = player;
    } else {
      this.away = player;
    }
  };

  this.getPlayer = function (homeAway) {
    if (homeAway === 'home') {
      return this.home;
    } else {
      return this.away;
    }
  };

  this.getOtherPlayer = function (homeAway) {
    if (homeAway === 'home') {
      return this.away;
    } else {
      return this.home;
    }
  };

  this.movePlayer = function (player, x) {
    player.x = x;
    player.lastUpdate = Date.now();
  };

  this.projectIntoLocal = function (observerHomeAway, x, y) {
    if (observerHomeAway === 'home') {
      return [x,y];
    } else {
      return [-x, -y];
    }
  };

  this.tick = function() {
    this.ball.x += this.ball.velocityX;
    this.ball.y += this.ball.velocityY;

    if (this.ball.x <= -200 || this.ball.x >= 200) {
      this.ball.velocityX *= -1;
    }

    if (this.ball.y <= -200 || this.ball.y >= 200) {
      this.ball.velocityY *= -1;
    }
  };
};
