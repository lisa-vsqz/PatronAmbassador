const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

app.post('/process', (req, res) => {
    const data = req.body;
    const processedData = { message: `Hello, ${data.name} from Node.js service!` };
    res.json(processedData);
});

app.listen(3000, () => {
    console.log('Node.js service listening on port 3000');
});
