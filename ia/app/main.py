from fastapi import FastAPI

app = FastAPI(
    title="Absence IA Service",
    description="Service de reconnaissance faciale - FSTG",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "IA - Reconnaissance Faciale"}