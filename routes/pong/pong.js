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

router
  .get('/api/login', function (req, res) {
    const newPlayer = new PongPlayer();
    runningGame.addPlayer(newPlayer);

    res.send(newPlayer.id.toString());
  });

router
  .get('/api/move', function (req, res) {
    const data = decodePythonDict(req.query.data);
    runningGame.movePlayer(data.player, data.x);

    const other = runningGame.getOtherPlayer(data.player);

    const otherX = other ? Math.floor(other.x) : 0;
    res.send(otherX.toString());
  });

module.exports = router;
