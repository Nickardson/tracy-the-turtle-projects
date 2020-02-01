const PongPlayer = require('./PongPlayer');

module.exports = function () {
  this.players = [];

  this.addPlayer = function (player) {
    // Add player, allowing only the latest 2 to join
    // this.players = this.players.concat([player]).slice(-2);
    this.players.unshift(player);
  };

  this.movePlayer = function (id, x) {
    const player = this.players.find(p => p.id === id);
    player.x = x;
    player.lastUpdate = Date.now;

    this.players.sort((a, b) => {
      return b.lastUpdate - a.lastUpdate;
    });
  };

  this.getOtherPlayer = function (id) {
    return this.players.find(p => p.id !== id);
  };

  this.addPlayer(new PongPlayer());
  this.addPlayer(new PongPlayer());
};
