const PongPlayer = require('./PongPlayer');
const PongBall = require('./PongBall');

module.exports = function () {
  this.home = new PongPlayer(true, true);
  this.away = new PongPlayer(false, true);

  this.ball = new PongBall();

  this.paddleSeparation = 140;
  this.paddleWidth = 50;
  this.paddleHeight = 10;
  this.ballRadius = 10;

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
      return [x, y];
    } else {
      return [-x, -y];
    }
  };

  this.tick = function () {
    this.ball.x += this.ball.velocityX;
    this.ball.y += this.ball.velocityY;

    // Bounce off left-right walls
    if (this.ball.x <= -200 + this.ballRadius || this.ball.x >= 200 - this.ballRadius) {
      this.ball.velocityX *= -1;
    }

    // Home player failed
    if (this.ball.y < -200 + this.ballRadius) {
      this.away.score++;
      this.ball.velocityY = this.ball.baseSpeedY;
      // this.ball.y = -200 + this.ballRadius;
    }
    // Away player failed
    if (this.ball.y > 200 - this.ballRadius) {
      this.home.score++;
      this.ball.velocityY = -this.ball.baseSpeedY;
      // this.ball.y = 200 - this.ballRadius;
    }

    // Home player hit?
    if (Math.abs(this.ball.x - this.home.x) < this.paddleWidth / 1.2 && this.ball.y <= -this.paddleSeparation) {
      this.ball.y = -this.paddleSeparation + this.paddleHeight + this.ballRadius;
      this.ball.velocityY *= -1;
      // this.ball.velocityY *= -1.1;
    }

    // Away player hit?
    if (Math.abs(-this.ball.x - this.away.x) < this.paddleWidth / 1.2 && this.ball.y >= this.paddleSeparation) {
      this.ball.y = this.paddleSeparation - this.paddleHeight - this.ballRadius;
      this.ball.velocityY *= -1;
      // this.ball.velocityY *= -1.1;
    }

    if (this.home.isAI) {
      this.playerAI(this.home);
    }
    if (this.away.isAI) {
      this.playerAI(this.away);
    }
  };

  this.playerAI = function (player) {
    const [ballLocalX] = this.projectIntoLocal(this.home ? 'away' : 'home', this.ball.x, this.ball.y);
    player.x = ballLocalX;
  };
};
