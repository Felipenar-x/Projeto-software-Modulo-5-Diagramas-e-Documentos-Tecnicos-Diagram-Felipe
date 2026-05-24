# DoculA Diagram API

## Descrição

O **DoculA Diagram API** é um microsserviço responsável por gerar diagramas técnicos em **PlantUML** a partir de dados estruturados enviados pelo **Gateway API**.

Este serviço faz parte do **Módulo 5 — Diagramas e Documentos Técnicos** da plataforma **DoculA**.

## Objetivo

O serviço recebe JSON estruturado e retorna PlantUML textual para:

- UML de Classes;
- relacionamentos entre classes;
- arquitetura de sistema;
- arquitetura cloud;
- perfis de usuário;
- fluxo de processo.

## Arquitetura

Fluxo principal do Módulo 5:

```txt
Frontend
   ↓
Gateway API
   ↓
Parser API
   ↓
Diagram API
```

Fluxo de geração de diagramas:

```txt
Parser API → Dados estruturados → Diagram API → PlantUML
```

O **Diagram API** não é consumido diretamente pelo usuário final. Ele é chamado pelo **Gateway API**, que centraliza a comunicação com o frontend e com os demais serviços do módulo.

## Deploy em produção

Diagram API:

```txt
https://diagramas-diagram-eugce0h0bygfdqhf.canadacentral-01.azurewebsites.net
```

Swagger/OpenAPI do Diagram API:

```txt
https://diagramas-diagram-eugce0h0bygfdqhf.canadacentral-01.azurewebsites.net/docs
```

Gateway API:

```txt
https://docula-gateway-api-dzgfg8ghghadeedd.eastus-01.azurewebsites.net/
```

Parser API:

```txt
https://diagramas-parser-e6dzc7f5ateae3ce.canadacentral-01.azurewebsites.net
```

## Requisitos

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic
- PlantUML textual

## Instalação local

```bash
pip install -r requirements.txt
```

## Como executar localmente

```bash
python -m uvicorn app.main:app --reload
```

A aplicação ficará disponível em:

```txt
http://127.0.0.1:8000
http://127.0.0.1:8000/docs
```

Caso rode junto com os outros serviços do Módulo 5, recomenda-se usar a porta `8002`:

```bash
python -m uvicorn app.main:app --reload --port 8002
```

## Endpoints principais

- `GET /health`
- `POST /generate/uml`
- `POST /generate/architecture`
- `POST /generate/cloud`
- `POST /generate/profiles`
- `POST /generate/flow`

## Health check

```http
GET /health
```

Resposta:

```json
{
  "status": "ok",
  "service": "docula-diagram-api",
  "version": "1.0.0"
}
```

## POST /generate/uml

Gera UML de Classes a partir de classes, atributos, métodos e relacionamentos.

Exemplo de entrada:

```json
{
  "classes": [
    {
      "name": "Usuario",
      "attributes": ["nome", "email"],
      "methods": ["login", "logout"]
    },
    {
      "name": "Pedido",
      "attributes": ["usuario"],
      "methods": ["finalizar"]
    }
  ],
  "relationships": [
    {
      "from_class": "Pedido",
      "to_class": "Usuario",
      "type": "association"
    }
  ]
}
```

Exemplo de resposta:

```json
{
  "plantuml": "@startuml\nclass Usuario {\n  nome\n  email\n  login()\n  logout()\n}\n\nclass Pedido {\n  usuario\n  finalizar()\n}\n\nPedido --> Usuario\n@enduml"
}
```

## Relacionamentos UML suportados

- `inheritance` → `--|>`
- `implementation` → `..|>`
- `association` → `-->`
- `dependency` → `..>`

Exemplo:

```txt
Pedido --|> Entidade
UsuarioService ..|> IService
Pedido --> Usuario
Controller ..> Service
```

## POST /generate/architecture

Gera um PlantUML de arquitetura do sistema do Módulo 5.

Entrada:

```json
{
  "project_id": "10",
  "project_name": "Projeto DoculA"
}
```

Saída esperada contém:

```json
{
  "diagram_type": "architecture",
  "plantuml": "@startuml\n..."
}
```

## POST /generate/cloud

Gera uma visão cloud/Azure com App Services e banco.

Entrada:

```json
{
  "project_id": "10",
  "project_name": "Projeto DoculA"
}
```

Saída esperada contém:

```json
{
  "diagram_type": "cloud",
  "plantuml": "@startuml\n..."
}
```

## POST /generate/profiles

Gera diagrama de perfis/atores do módulo.

Entrada:

```json
{
  "project_id": "10",
  "project_name": "Projeto DoculA",
  "profiles": ["Desenvolvedor", "Tech Lead", "Gerente de Projetos"]
}
```

Saída esperada contém:

```json
{
  "diagram_type": "profiles",
  "plantuml": "@startuml\nactor \"Desenvolvedor\" as P1\n..."
}
```

O PlantUML gerado contém actors e usecases.

## POST /generate/flow

Gera um fluxo de processo da geração de diagramas.

Entrada:

```json
{
  "project_id": "10",
  "project_name": "Projeto DoculA"
}
```

Saída esperada contém:

```json
{
  "diagram_type": "flow",
  "plantuml": "@startuml\nstart\n..."
}
```

O PlantUML gerado contém `start` e `stop`.

## Integração com Parser API

- O **Parser API** extrai classes, atributos, métodos e relacionamentos.
- O **Gateway API** envia esses dados para o **Diagram API**.
- O **Diagram API** transforma JSON estruturado em PlantUML.

## Integração com Gateway API

- O frontend não chama o **Diagram API** diretamente.
- O **Gateway API** é o ponto central de comunicação do Módulo 5.
- O **Gateway API** chama o **Diagram API** nos endpoints `/generate/*`.
- O **Gateway API** retorna o PlantUML para o frontend e pode salvar histórico.

## Integração com Módulo 1 e Módulo 2

- O **Diagram API** não valida JWT diretamente.
- A validação JWT do **Módulo 1** é feita no **Gateway API**.
- O acesso aos artefatos do **Módulo 2** também é feito pelo **Gateway API**.
- O **Diagram API** apenas recebe os dados já estruturados e gera o PlantUML.

## Tecnologias utilizadas

- Python
- FastAPI
- Uvicorn
- Pydantic
- PlantUML
- Swagger/OpenAPI
- Azure App Service

## Deploy

O serviço está preparado para execução em **Azure App Service**.

Startup command:

```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Versionamento

Versão final:

```txt
v1.0.0
```

Histórico:

```txt
v0.1.0 - Primeira versão funcional do gerador PlantUML
v0.1.1 - Preparação para deploy Azure
v0.2.0 - Adição de diagramas arquiteturais, cloud, perfis e fluxo
v0.3.0 - Renderização de relacionamentos UML
v1.0.0 - Versão final do Diagram API para entrega do Módulo 5
```

## Status atual

```txt
Diagram API online
UML de Classes funcionando
Relacionamentos UML funcionando
Arquitetura de sistema funcionando
Arquitetura cloud funcionando
Perfis de usuário funcionando
Fluxo de processo funcionando
Integração com Gateway funcionando
Deploy em Azure funcionando
```
