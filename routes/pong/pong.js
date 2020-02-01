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
    const otherX = other ? Math.floor(other.x) : 0;
    const ball = runningGame.ball;
    res.send(`${otherX},${ball.x},${ball.y},${ball.velocityX},${ball.velocityY}`);
  });

module.exports = router;
