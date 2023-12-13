# JSON2RDF

## Steps to run JSON2RDF

#### Step 1
- Create .env file similar to .env_example for defining ports
  Note: Mapper port cannot be changed it should be 4000 

- Docker build and run 
```
    docker compose build --no-cache
    docker up
    
```


Visit - http://localhost:{CONV_PORT}/docs for available endpoints and swagger docs