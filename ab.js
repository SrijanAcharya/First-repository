const express = require('express');
const port = process.env.PORT || 3000;
const app = express()
app.listen(port,() =>{
    console.log(`Running in port: ${port}`)
})
app.get('/',(req,res)=>{
    res.send('Hello World!')
})
app.get('/',(req,res)=>{
    res.send('Hello World! And its worst creations!')
})