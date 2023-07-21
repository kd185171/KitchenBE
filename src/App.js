const express = require("express");
const bodyParser = require("body-parser");
const KitchenController = require("./KitchenController");

const app = express();
const port = 3000;

app.use(bodyParser.json());


app.get("/", (req, res) => {
  const controller = new KitchenController();
  controller.convertArrayToJSON(req, res);
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
