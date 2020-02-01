let incrementingId = 0;

module.exports = function (isHome) {
  this.id = ++incrementingId;
  this.x = 0;
  this.lastUpdate = Date.now();

  // Home or Away
  this.home = isHome;

  this.score = 0;
};
