const dummyjson = require('dummy-json');
const service = module.exports = {};

/**
 * Client can receive travel info status.
 * @param {object} ws WebSocket connection.
 */
service.travelInfo = async (ws) => {
  (function myLoop (i) {
  setTimeout(() => {
      ws.send(generateResponse());
      if (--i) myLoop(i);
  }, 1000);
  }(100));  

  function generateResponse() {
  const template = `{
      "destination": "{{city}}",
      "arrival": "{{int 2 6}}h",
      "distance": "{{int 18 65}}km"
  }`;
  return dummyjson.parse(template);
  }
  
};
