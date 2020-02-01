const express = require('express');
const router = express.Router();

const PongPlayer = require('./PongPlayer');

let players = [];

router
  .use(express.static('routes/pong'));

router
  .get('/api/login', function (req, res) {
    const newPlayer = new PongPlayer();

    // Add player, kicking off the oldest player
    players.push(newPlayer);
    players = players.slice(-2);

    res.send(newPlayer.id.toString());
  });

module.exports = router;
