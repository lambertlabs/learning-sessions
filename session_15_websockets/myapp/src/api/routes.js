const util = require('util');
const { Router } = require('express');
const { pathParser } = require('../lib/path');
const { yellow } = require('../lib/colors');
const { travelInfo } = require('./services/travel-status');
const router = Router();
module.exports = router;
router.ws('/travel-status', async (ws, req) => {
  const path = pathParser(req.path);
  console.log(`${yellow(path)} client connected.`);
  await travelInfo(ws);
});
