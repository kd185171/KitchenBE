const KitchenService = require("./KitchenService");

class KitchenController {
  constructor() {
    this.KitchenService = new KitchenService();
  }

  convertArrayToJSON(req, res) {
    const inputArray = [
      'Monday:"pizza","burger"',
      'Tuesday:"Drinks","Juice"',
    ];

    const convertedJSON = this.KitchenService.convertToJSON(inputArray);
    res.json(convertedJSON);
  }
}

module.exports = KitchenController;
