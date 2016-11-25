const skygearCloud = require('skygear/cloud');
const handler = require('./src/handler');
const Provider = require('./src/provider');
console.log(Provider);

skygearCloud.provides('auth', 'com.facebook', Provider);

skygearCloud.op('op1', function(opts) {
  console.log('op1');
  console.log(opts);
  return {
    'status': 'ok'
  };
});