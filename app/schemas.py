from pydantic import BaseModel
from typing import List, Optional


class UMLClass(BaseModel):
    name: str
    attributes: List[str]
    methods: List[str]


class UMLRequest(BaseModel):
    classes: List[UMLClass]


class UMLResponse(BaseModel):
    plantuml: str


class GenericDiagramRequest(BaseModel):
    project_id: Optional[str] = None
    project_name: Optional[str] = "Projeto DoculA"
    description: Optional[str] = None
    services: Optional[List[str]] = None
    profiles: Optional[List[str]] = None


class GenericDiagramResponse(BaseModel):
    diagram_type: str
    project_id: Optional[str] = None
    project_name: Optional[str] = None
    plantuml: str