const express = require('express');
const router = express.Router();

router
  // Add a binding to handle '/test'
  .get('/', function (req, res) {
    // render the /tests view
    res.send('<p>Wooo</p>');
  })

// Import my automated routes into the path '/tests/automated'
// This works because we're already within the '/tests' route so we're simply appending more routes to the '/tests' endpoint
// .use('/automated', automatedRoutes);

module.exports = router;
