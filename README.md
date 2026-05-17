# DoculA Diagram API

Microsserviço responsável por gerar diagramas UML em formato **PlantUML** a partir de dados estruturados extraídos do código-fonte.

Este serviço faz parte do **Módulo 5 — Diagramas e Documentos Técnicos** da plataforma DoculA, uma solução de documentação inteligente baseada em microsserviços.

## Objetivo

O objetivo deste microsserviço é receber informações estruturadas sobre classes, atributos e métodos e transformar esses dados em um diagrama UML no formato PlantUML.

Este serviço é consumido pelo **Gateway API**, que orquestra o fluxo entre:

```txt
Frontend → Gateway API → Parser API → Diagram API
````

## Arquitetura do módulo

```txt
Frontend
   ↓
Gateway API
   ↓
Parser API
   ↓
Diagram API
```

Responsabilidade deste serviço:

```txt
Receber JSON estruturado → Gerar PlantUML → Retornar diagrama textual
```

## Funcionalidades atuais

* Geração de diagrama UML de classes em PlantUML;
* Recebimento de classes, atributos e métodos em JSON;
* Endpoint de health check;
* Documentação automática via Swagger/OpenAPI;
* Preparado para deploy em Azure App Service.

## Funcionalidades futuras

* Exportação de diagramas em PNG;
* Exportação em SVG;
* Melhorias visuais nos diagramas;
* Suporte a relacionamentos entre classes;
* Suporte a outros tipos de diagramas UML;
* Integração com IA para melhorar a interpretação arquitetural.

## Endpoints

### Health check

```http
GET /health
```

Exemplo de resposta:

```json
{
  "status": "ok",
  "service": "docula-diagram-api"
}
```

### Gerar diagrama UML

```http
POST /generate/uml
```

Exemplo de entrada:

```json
{
  "classes": [
    {
      "name": "Usuario",
      "attributes": ["nome", "email"],
      "methods": ["login", "logout"]
    }
  ]
}
```

Exemplo de resposta:

```json
{
  "plantuml": "@startuml\nclass Usuario {\n  nome\n  email\n  login()\n  logout()\n}\n@enduml"
}
```

## Como executar localmente

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Executar a aplicação

```bash
python -m uvicorn app.main:app --reload
```

A aplicação ficará disponível em:

```txt
http://127.0.0.1:8000
```

Swagger/OpenAPI:

```txt
http://127.0.0.1:8000/docs
```

## Deploy

Este serviço está preparado para deploy na Azure App Service.

Startup command utilizado:

```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Tecnologias utilizadas

* Python
* FastAPI
* Uvicorn
* Pydantic
* PlantUML

## Versionamento

O projeto utiliza versionamento semântico.

Versão atual:

```txt
v0.1.1
```

Histórico inicial:

```txt
v0.1.0 - Primeira versão funcional do gerador PlantUML
v0.1.1 - Preparação para deploy na Azure
```

## Papel na integração

Este microsserviço não é consumido diretamente pelo usuário final.

Ele é chamado pelo **Gateway API**, que recebe requisições do frontend, chama o Parser API para extrair informações do código e depois chama este serviço para gerar o PlantUML.

Fluxo completo:

```txt
Usuário → Frontend → Gateway API → Parser API → Diagram API → Gateway API → Frontend
```

