class KitchenService {
    convertToJSON(array) {
      const result = {};
  
      array.forEach(item => {
        const [day, values] = item.split(":");
        result[day] = values.split(",").map(value => value.replace(/"/g, ""));
      });
  
      return result;
    }
  }
  
  module.exports = KitchenService;
  