from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import UMLRequest, UMLResponse
from app.services.plantuml_generator import generate_plantuml

app = FastAPI(
    title="DoculA Diagram API",
    description="Microsserviço responsável por gerar diagramas UML em PlantUML.",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "docula-diagram-api"
    }


@app.post("/generate/uml", response_model=UMLResponse)
def generate_uml(request: UMLRequest):

    plantuml = generate_plantuml(request.classes)

    return {
        "plantuml": plantuml
    }