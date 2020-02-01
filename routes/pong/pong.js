const express = require('express');
const router = express.Router();

const PongGame = require('./PongGame');
const PongPlayer = require('./PongPlayer');

const runningGame = new PongGame();

router
  .use(express.static('routes/pong'));

router
  .get('/api/login', function (req, res) {
    const newPlayer = new PongPlayer();
    runningGame.addPlayer(newPlayer);

    res.send(newPlayer.id.toString());
  });

module.exports = router;
