def generate_plantuml(classes):
    lines = ["@startuml"]

    for cls in classes:
        lines.append(f"class {cls.name} {{")

        for attr in cls.attributes:
            lines.append(f"  {attr}")

        for method in cls.methods:
            lines.append(f"  {method}()")

        lines.append("}")

    lines.append("@enduml")

    return "\n".join(lines)


def generate_architecture_plantuml(project_name: str | None = None):
    title = project_name or "Projeto DoculA"

    return f"""@startuml
title Arquitetura do Sistema - {title}

skinparam componentStyle rectangle

package "Frontend" {{
  [Interface Web]
}}

package "Backend - Módulo 5" {{
  [Gateway API]
  [Parser API]
  [Diagram API]
}}

database "PostgreSQL" as DB

[Interface Web] --> [Gateway API]
[Gateway API] --> [Parser API]
[Gateway API] --> [Diagram API]
[Gateway API] --> DB

@enduml"""


def generate_cloud_plantuml(project_name: str | None = None):
    title = project_name or "Projeto DoculA"

    return f"""@startuml
title Arquitetura Cloud - {title}

cloud "Azure" {{
  node "Azure App Service\\nFrontend" as FE
  node "Azure App Service\\nGateway API" as GW
  node "Azure App Service\\nParser API" as PA
  node "Azure App Service\\nDiagram API" as DA
  database "Azure PostgreSQL" as DB
}}

FE --> GW
GW --> PA
GW --> DA
GW --> DB

@enduml"""


def generate_profiles_plantuml(project_name: str | None = None, profiles=None):
    title = project_name or "Projeto DoculA"

    if not profiles:
        profiles = ["Desenvolvedor", "Tech Lead", "Gerente de Projetos", "Usuário"]

    lines = [
        "@startuml",
        f"title Perfis de Usuário - {title}",
        "",
        'rectangle "Módulo de Diagramas" {',
        '  usecase "Gerar Diagrama UML" as UC1',
        '  usecase "Visualizar Documentação de API" as UC2',
        '  usecase "Consultar Histórico do Projeto" as UC3',
        '  usecase "Analisar Código com IA" as UC4',
        "}",
        ""
    ]

    aliases = []

    for index, profile in enumerate(profiles, start=1):
        alias = f"P{index}"
        aliases.append(alias)
        lines.append(f'actor "{profile}" as {alias}')

    lines.append("")

    for alias in aliases:
        lines.append(f"{alias} --> UC1")
        lines.append(f"{alias} --> UC2")
        lines.append(f"{alias} --> UC3")
        lines.append(f"{alias} --> UC4")

    lines.append("@enduml")

    return "\n".join(lines)


def generate_flow_plantuml(project_name: str | None = None):
    title = project_name or "Projeto DoculA"

    return f"""@startuml
title Fluxo de Geração de Diagramas - {title}

start
:Usuário acessa um projeto;
:Seleciona o Módulo de Diagramas;
:Informa ou cola código-fonte;
:Frontend envia requisição ao Gateway API;
:Gateway envia código ao Parser API;
:Parser extrai classes, métodos, atributos ou endpoints;
:Gateway envia dados ao Diagram API;
:Diagram API gera PlantUML;
:Gateway salva histórico no banco;
:Frontend exibe o resultado ao usuário;
stop

@enduml"""