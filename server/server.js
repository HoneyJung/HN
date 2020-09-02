const express = require('express')
var engines = require('consolidate');

const app = express()
const port = 3000
const path = require('path');
app.engine('html', engines.hogan);
app.set('view engine', 'html');
app.set('views', 'views');

app.get('/', (req, res) => {
    res.render('index.html')
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})
