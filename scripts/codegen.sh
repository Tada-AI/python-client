#! /bin/bash

npx @openapitools/openapi-generator-cli generate \
    -i http://localhost:4000/api-json \
    -g python \
    -o . \
    --additional-properties=packageName=tada_ai 
