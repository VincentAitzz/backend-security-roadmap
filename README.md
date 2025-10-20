README.md (resumen ejecutivo)
# Backend Security Roadmap — Día 1

Estructura modular de proyecto FastAPI con logging JSON, rutas separadas y middleware.

## Ejecución

1. Instala dependencias:
   ```bash
   poetry install


Corre el servidor:

poetry run uvicorn app.main:app --reload --port 8000


Endpoints:

GET /status

GET /greet?name=TuNombre

POST /echo

GET /secure-data (header X-API-Key: mysecretkey)

Documentación: http://127.0.0.1:8000/docs

Logging

El sistema de logging usa formato JSON:

{"message": "Request processed", "method": "GET", "path": "/status", "status": 200, "time_ms": 0.67}


---

# ▶️ **Cómo ejecutarlo ahora que `main.py` está dentro de `app/`**

En la raíz del proyecto (donde está tu archivo `pyproject.toml`), usa:

```bash
poetry run uvicorn app.main:app --reload --port 8000