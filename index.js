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

skygearCloud.op('op2', function(opts) {
  console.log('op2');
  console.log(opts);
  return {
    'status': 'ok'
  };

skygearCloud.op('op3', function(opts) {
  console.log('op3');
  console.log(opts);
  return {
    'status': 'ok'
  };
});
