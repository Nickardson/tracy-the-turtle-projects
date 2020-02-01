module.exports = function () {
  this.players = [];

  this.addPlayer = function (player) {
    // Add player, allowing only the latest 2 to join
    this.players = this.players.concat([player]).slice(-2);
  };
};
