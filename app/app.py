from fastapi import FastAPI

app = FastAPI()


@app.get("/api/healthcheck")
def healthcheck():
    """Healthcheck endpoint to check if the service is up and running."""
    return {"message": "Service is up and running!"}


@app.get("/")
def root():
    """Root endpoint to check if the service is up and running."""
    return {"message": "FastAPI CRUD"}
