const express = require('express');
const app = express()

app.get("/", (req, res, next) => {
    res.send("hello world")
})

const port = 3000;


app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})