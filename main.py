from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Create the specific "App" instance. 
# This 'app' object is what runs your whole backend.
app = FastAPI()


# --- MIDDLEWARE ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows ANY website to talk to this backend (OK for local dev)
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],
)

# --- ROUTES ---
# A "Route" tells the code what to do when a user visits a specific URL.

# 1. The Root Route ("/")
# When someone visits http://localhost:8000/, this function runs.
@app.get("/")
def read_root():
    # We return a "Dictionary" (key-value pairs). 
    # FastAPI automatically converts this to JSON format.
    return {"message": "Welcome to DevOpsHub Backend"}

# 2. The Health Check Route ("/health")
# Kubernetes will use this later to ask: "Are you alive?"
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# 3. The Pipeline Route ("/api/pipelines")
# Later, we will get this data from Jenkins. 
# For now, we are "mocking" (faking) the data to test our Frontend.
@app.get("/api/pipelines")
def get_pipelines():
    return [
        {"id": 1, "name": "backend-build", "status": "SUCCESS", "last_run": "10 mins ago"},
        {"id": 2, "name": "frontend-deploy", "status": "FAILED", "last_run": "2 hours ago"},
        {"id": 3, "name": "infra-provision", "status": "RUNNING", "last_run": "Just now"},
    ]
