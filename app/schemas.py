from pydantic import BaseModel
from typing import List


class UMLClass(BaseModel):
    name: str
    attributes: List[str]
    methods: List[str]


class UMLRequest(BaseModel):
    classes: List[UMLClass]


class UMLResponse(BaseModel):
    plantuml: str