let incrementingId = 0;

module.exports = function () {
  this.id = ++incrementingId;
};
