const PongPlayer = require('./PongPlayer');

module.exports = function () {
  this.players = [];

  this.addPlayer = function (player) {
    // Add player, allowing only the latest 2 to join
    // this.players = this.players.concat([player]).slice(-2);
    this.players.push(player);
  };

  this.movePlayer = function (id, x) {
    const player = this.players.find(p => p.id === id);
    if (!player) {
      return;
    }

    player.x = x;
    player.lastUpdate = Date.now();

    this.players = this.players.filter(p => p.lastUpdate > player.lastUpdate - 1000);
  };

  this.getOtherPlayer = function (id) {
    return this.players.find(p => p.id !== id);
  };

  this.addPlayer(new PongPlayer());
  this.addPlayer(new PongPlayer());
};
