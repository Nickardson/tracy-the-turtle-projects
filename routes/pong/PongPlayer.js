let incrementingId = 0;

module.exports = function (isHome, isAI) {
  this.id = ++incrementingId;
  this.x = 0;
  this.lastUpdate = Date.now();

  // Home or Away
  this.home = isHome;

  this.isAI = !!isAI;

  this.score = 0;
};
