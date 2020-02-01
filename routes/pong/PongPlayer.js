let incrementingId = 0;

module.exports = function () {
  this.id = ++incrementingId;
  this.x = 0;
  this.lastUpdate = Date.now();
};
