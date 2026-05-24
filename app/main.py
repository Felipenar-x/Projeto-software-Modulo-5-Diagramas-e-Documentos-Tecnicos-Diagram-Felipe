from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import (
    UMLRequest,
    UMLResponse,
    GenericDiagramRequest,
    GenericDiagramResponse
)

from app.services.plantuml_generator import (
    generate_plantuml,
    generate_architecture_plantuml,
    generate_cloud_plantuml,
    generate_profiles_plantuml,
    generate_flow_plantuml
)

app = FastAPI(
    title="DoculA Diagram API",
    description="Microsserviço responsável por gerar diagramas técnicos em PlantUML.",
    version="1.0.0"
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
        "service": "docula-diagram-api",
        "version": "1.0.0"
    }


@app.post("/generate/uml", response_model=UMLResponse)
def generate_uml(request: UMLRequest):
    plantuml = generate_plantuml(
    request.classes,
    request.relationships
)

    return {
        "plantuml": plantuml
    }


@app.post("/generate/architecture", response_model=GenericDiagramResponse)
def generate_architecture(request: GenericDiagramRequest):
    plantuml = generate_architecture_plantuml(request.project_name)

    return {
        "diagram_type": "architecture",
        "project_id": request.project_id,
        "project_name": request.project_name,
        "plantuml": plantuml
    }


@app.post("/generate/cloud", response_model=GenericDiagramResponse)
def generate_cloud(request: GenericDiagramRequest):
    plantuml = generate_cloud_plantuml(request.project_name)

    return {
        "diagram_type": "cloud",
        "project_id": request.project_id,
        "project_name": request.project_name,
        "plantuml": plantuml
    }


@app.post("/generate/profiles", response_model=GenericDiagramResponse)
def generate_profiles(request: GenericDiagramRequest):
    plantuml = generate_profiles_plantuml(
        project_name=request.project_name,
        profiles=request.profiles
    )

    return {
        "diagram_type": "profiles",
        "project_id": request.project_id,
        "project_name": request.project_name,
        "plantuml": plantuml
    }


@app.post("/generate/flow", response_model=GenericDiagramResponse)
def generate_flow(request: GenericDiagramRequest):
    plantuml = generate_flow_plantuml(request.project_name)

    return {
        "diagram_type": "flow",
        "project_id": request.project_id,
        "project_name": request.project_name,
        "plantuml": plantuml
    }
