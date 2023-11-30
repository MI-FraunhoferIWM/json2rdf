#!/bin/sh
# add port form env to config.json
echo $(cat config.json | jq '."baseURL" = "http://localhost:4000"') > config.json
cat ./config.json
./bin/cli.js