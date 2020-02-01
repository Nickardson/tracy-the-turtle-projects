const express = require('express');
const router = express.Router();

const PongGame = require('./PongGame');
const PongPlayer = require('./PongPlayer');

const runningGame = new PongGame();

function decodePythonDict(str) {
  return JSON.parse(str.replace(/'/g, '"'));
}

router
  .use(express.static('routes/pong'));

var nextIsHome = true;
router
  .get('/api/login', function (req, res) {
    const newPlayer = new PongPlayer(nextIsHome);
    nextIsHome = !nextIsHome;
    runningGame.addPlayer(newPlayer);

    res.send(newPlayer.home ? 'home' : 'away');
  });

router
  .get('/api/move', function (req, res) {
    const data = decodePythonDict(req.query.data);
    const player = runningGame.getPlayer(data.player);

    runningGame.movePlayer(player, data.x);

    const other = runningGame.getOtherPlayer(data.player);
    const [otherX] = other ? runningGame.projectIntoLocal('away', other.x, other.y) : [0, NaN];

    const ball = runningGame.ball;
    const [ballX, ballY] = runningGame.projectIntoLocal(data.player, ball.x, ball.y);
    const [ballVelocityX, ballVelocityY] = runningGame.projectIntoLocal(data.player, ball.velocityX, ball.velocityY);

    res.send(`${otherX},${ballX},${ballY},${ballVelocityX},${ballVelocityY}`);
  });

setInterval(() => {
  runningGame.tick();
}, 1000 / 30 * 10);

module.exports = router;
