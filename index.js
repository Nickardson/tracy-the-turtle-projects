const express = require('express')
const app = express()
const http = require('http')
const fs = require('fs')
const cors = require('cors');
const marked = require('marked');
const highlight = require('highlight.js');
const port = 8080

marked.setOptions({
  gfm: true,
  highlight: function (code) {
    return require('highlight.js').highlightAuto(code).value;
  },
});

app.use(cors());

app.get('/script/:name', function (req, res) {
  var templatePath = __dirname + '/public/scriptembed.html';
  var scriptPath = __dirname + `/scripts/${req.params.name}.py`;
  fs.readFile(templatePath, 'utf8', function (err, templateData) {
    if (err) {
      console.log(err);
    }
    fs.readFile(scriptPath, 'utf8', function (err, scriptData) {
      if (err) {
        console.log(err);
      }
      const highlighted = marked("```python\n" + scriptData + "\n```");
      res.send(templateData.toString().replace("{code}", highlighted));
    });
  });
});

const pongRoutes = require('./routes/pong');
app.use('/pong', pongRoutes)

app.use(express.static('public'));
// app.use('/320x', express.static('public'));
app.route(/\/320x/)
  .get((req, res, next) => {
    res.redirect(req.url.replace(/https?:\/\//, '../'));
    // res.send('Hey')
  });

const httpsOptions = {
  key: fs.readFileSync('./localhost+2-key.pem'),
  cert: fs.readFileSync('./localhost+2.pem'),
};

// http.createServer()
// var serverType = https;
var serverType = http;
const server = serverType.createServer(httpsOptions, app)
  .listen(port, () => {
    console.log('server running at ' + port);
  });
