# Phase 2 - Basic App Funtion and Containerization

Phase 2 focused on building the foundation by creating a simple app function, containerizing the app, and validating it's functionality by testing the containerized app locally. 

## Objectives:

1. Create a Python function that prints the current app version and exits.
2. Use Semantic Versioning.
3. Containerize the app using Docker.
4. Build and test run the app container locally and ensure it returns the correct value.


## Work Done

- Created a version function that prints the version ```v0.0.1``` and exits.
- Validated that the version function worked as expected.

- A Dockerfile was created:

   - Used a lightweight base image Python:3.11-slim
   - Set the correct working directory
   - Installed dependencies using a ```requirements.txt``` file
   - Copied app code to working directory in container
   - Ran the Python function via the ```main.py``` file
  
 <br/>
     
        ```dockerfile
        FROM python:3.11-slim
        
        WORKDIR /app
        
        COPY requirements.txt .
        
        RUN pip install --no-cache-dir -r requirements.txt
        
        COPY . .
        
        CMD ["python", "app/main.py"]
        ```
<br/>

Built the app image locally using:

```bash
docker build -t hivebox-app:v0.0.1 .
```
Ran and tested the app container locally:

```bash
docker run --name hivebox hivebox-app:v0.0.1
```
Visited ```localhost:5000/version``` to verify the containerized app worked correctly.

<br/>

## Tools:

- Git
- VS Code
- Docker

## Notes:

- App version (v0.0.1) was aligned with Dockerfile versioning and tags to ensure clarity and traceability.
- Project planning and tracking done via GitHub Kanban.
- Used basic feature branching strategy for clearer separation of concerns: ```version-function``` handled app code and ```feature/docker-setup``` handled all containerization tasks for Phase 2.

# What's Next?

Phase 3 will introduce:

- Flask endpoints for /version and /temperature
- Unit testing setup
- GitHub Actions for CI
- Docker image linting and build pipelines

