# 🛡️ Backend Security Roadmap

Proyecto educativo y práctico para aprender desarrollo **Backend con FastAPI** y **seguridad aplicada** paso a paso.

Incluye:
- Estructura modular profesional (rutas, middleware, core, utils).
- Logging en formato JSON (consola + archivo).
- CORS configurado correctamente.
- Cabeceras de seguridad HTTP.
- API Key con registro de intentos fallidos.
- Analizador de logs local.

---

## ⚙️ Ejecución del proyecto

Desde la raíz del proyecto (donde está `pyproject.toml`):

```bash
poetry install
poetry run uvicorn app.main:app --reload --port 8000
```

Documentación interactiva: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧩 Endpoints actuales

| Método | Ruta | Descripción |
|:-------|:------|:-------------|
| `GET` | `/status` | Estado general de la API |
| `GET` | `/greet?name=` | Saludo dinámico |
| `POST` | `/echo` | Devuelve datos enviados (modelo Pydantic) |
| `GET` | `/secure-data` | Protegido con header `X-API-Key` |
| `GET` | `/time` | Hora del servidor (UTC + local opcional) |

---

## 🧾 Sistema de logging

El sistema usa formato **JSON estructurado** para consola y archivo (`app_logs.jsonl`).

Ejemplo:
```json
{"message": "Request processed", "method": "GET", "path": "/status", "status": 200, "time_ms": 0.64}
```

### Logs de seguridad
Registra intentos válidos e inválidos al endpoint `/secure-data`:

```json
{"event": "unauthorized_access_attempt", "client_ip": "127.0.0.1", "status": 401}
```

---

## 🧠 Analizador de logs local

Script: `app/utils/log_analyzer.py`  
Permite revisar los intentos fallidos y las IPs involucradas.

Ejecución:
```bash
poetry run python app/utils/log_analyzer.py
```

Salida esperada:
```
🚨 Intentos no autorizados detectados: 5
🧠 IPs únicas involucradas:
 - 127.0.0.1
```

---

## 📅 Registro de avances

### 🗓️ Día 1 — Estructura y base del proyecto
- Configuración de entorno con **Poetry**.  
- Creación de estructura modular: `api/`, `core/`, `models/`, `main.py`.  
- Implementación de endpoints iniciales (`/status`, `/greet`, `/echo`, `/secure-data`).  
- Logging en formato JSON.  
- Primer commit profesional con convención **Conventional Commits**.

### 🗓️ Día 2 — Seguridad Web y Logging de auditoría
- Endpoint `/time` estandarizado (UTC + Epoch + zona local opcional).  
- Configuración de **CORS** con orígenes seguros (`localhost` y `127.0.0.1`).  
- Middleware con **cabeceras HTTP de seguridad**:  
  - `X-Frame-Options`, `X-Content-Type-Options`, `X-XSS-Protection`, `Referrer-Policy`.  
- Registro detallado de accesos **autorizados y no autorizados**.  
- Creación de log persistente (`app_logs.jsonl`).  
- Implementación de **analizador de logs local** con `ast.literal_eval()` para lectura segura.  
- Corrección del endpoint `/secure-data` y pruebas de CORS desde consola.  
- Commit:  
  ```
  feat(security): add CORS restrictions, security headers and unauthorized access analyzer
  ```

---

## 📘 Próximo paso — Día 3
**Autenticación con hashing y JWT**:
- Registro y autenticación de usuarios.  
- Hashing seguro con bcrypt.  
- Generación de tokens JWT.  
- Protección de rutas con autenticación basada en token.

---

## ✍️ Notas del autor

Este proyecto es parte de un **roadmap personal de desarrollo backend y ciberseguridad**, con aprendizaje práctico y registro progresivo diario.

---

📅 Última actualización: **Día 2 — 22 de octubre de 2025**
