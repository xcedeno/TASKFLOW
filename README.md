# 🧩 TaskFlow Backend

> 🌐 **English version below / Versión en español arriba**

---

## 🇪🇸 TaskFlow Backend (Español)

**TaskFlow** es un sistema backend escalable desarrollado con **FastAPI**, **PostgreSQL** y **Docker**, diseñado para la **gestión operativa del departamento de IT**, incorporando principios de **metodologías ágiles**, **calendarios de tareas**, **autenticación de usuarios** y **endpoints seguros** listos para integración con un frontend moderno.

---

### 🚀 Tecnologías principales

| Componente | Descripción |
|-------------|-------------|
| **Python 3.11** | Lenguaje principal del backend |
| **FastAPI** | Framework backend asíncrono y de alto rendimiento |
| **PostgreSQL 15** | Base de datos relacional |
| **SQLAlchemy** | ORM para modelado de datos |
| **Pydantic** | Validación de datos y serialización |
| **Docker & Docker Compose** | Contenedores y orquestación |
| **Uvicorn** | Servidor ASGI de producción |
| **Alembic (opcional)** | Migraciones de base de datos |

---

### 🏗️ Estructura del proyecto

```bash
taskflow/
├── app/
│   ├── main.py              # Punto de entrada de la aplicación FastAPI
│   ├── database.py          # Configuración y conexión a PostgreSQL
│   ├── models.py            # Modelos SQLAlchemy
│   ├── schemas.py           # Esquemas Pydantic
│   ├── crud.py              # Lógica CRUD
│   ├── auth.py              # Autenticación y JWT
│   ├── config.py            # Configuración del proyecto
│   └── Dockerfile           # Imagen del servicio web
│
├── requirements.txt         # Dependencias Python
├── docker-compose.yml       # Orquestación de contenedores
└── README.md                # Documentación del proyecto
```

---

### ⚙️ Configuración del entorno

```bash
git clone https://github.com/<tu-usuario>/taskflow-backend.git
cd taskflow-backend
```

Crea un archivo `.env` (opcional):

```
POSTGRES_USER=taskflow
POSTGRES_PASSWORD=taskflowpass
POSTGRES_DB=taskflow
SECRET_KEY=super-secret-change-me
DATABASE_URL=postgresql+psycopg2://taskflow:taskflowpass@db:5432/taskflow
```

> 💡 Nota: el `docker-compose.yml` ya exporta estas variables automáticamente.

---

### 🐳 Despliegue con Docker Compose

```bash
docker-compose up --build
```

Esto ejecutará:
- **PostgreSQL 15** en el puerto `5432`
- **FastAPI (Uvicorn)** en el puerto `8000`

Luego visita 👉 [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 🧠 Endpoints principales

| Método | Endpoint | Descripción |
|--------|-----------|-------------|
| `POST` | `/auth/register` | Crear nuevo usuario |
| `POST` | `/auth/login` | Iniciar sesión y obtener token JWT |
| `GET` | `/tasks/` | Listar tareas |
| `POST` | `/tasks/` | Crear nueva tarea |
| `PUT` | `/tasks/{id}` | Actualizar tarea |
| `DELETE` | `/tasks/{id}` | Eliminar tarea |
| `GET` | `/calendar/events` | Consultar eventos del calendario |
| `POST` | `/calendar/events` | Agregar evento al calendario |

---

### 🔒 Seguridad

- Autenticación con **JWT**
- Contraseñas cifradas con **bcrypt**
- Configuración segura mediante **variables de entorno**

---

### 👨‍💻 Autor

**Xavier Cedeño**  
Analista de Sistemas | DevOps & Full Stack Developer  
🚀 Apasionado por la innovación, automatización y el aprendizaje continuo.  
📫 [LinkedIn](https://www.linkedin.com) | [GitHub](https://github.com/<tu-usuario>)

---

## 🇬🇧 TaskFlow Backend (English)

**TaskFlow** is a scalable backend system built with **FastAPI**, **PostgreSQL**, and **Docker**, designed to support **IT department operations** with **agile methodology**, **task scheduling**, **user authentication**, and **secure API endpoints** ready for integration with modern frontends.

---

### 🚀 Core Technologies

| Component | Description |
|------------|-------------|
| **Python 3.11** | Main backend language |
| **FastAPI** | Asynchronous high-performance web framework |
| **PostgreSQL 15** | Relational database |
| **SQLAlchemy** | ORM for database models |
| **Pydantic** | Data validation and serialization |
| **Docker & Docker Compose** | Containerization and orchestration |
| **Uvicorn** | ASGI production server |
| **Alembic (optional)** | Database migrations |

---

### 🏗️ Project Structure

```bash
taskflow/
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── database.py          # PostgreSQL connection
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── crud.py              # CRUD operations
│   ├── auth.py              # JWT authentication
│   ├── config.py            # Configuration
│   └── Dockerfile           # Web service Docker image
│
├── requirements.txt         # Python dependencies
├── docker-compose.yml       # Container orchestration
└── README.md                # Project documentation
```

---

### ⚙️ Setup Instructions

```bash
git clone https://github.com/<your-username>/taskflow-backend.git
cd taskflow-backend
```

Create a `.env` file (optional):

```
POSTGRES_USER=taskflow
POSTGRES_PASSWORD=taskflowpass
POSTGRES_DB=taskflow
SECRET_KEY=super-secret-change-me
DATABASE_URL=postgresql+psycopg2://taskflow:taskflowpass@db:5432/taskflow
```

> These variables are already defined in `docker-compose.yml`.

---

### 🐳 Run with Docker Compose

```bash
docker-compose up --build
```

This runs:
- **PostgreSQL 15** on port `5432`
- **FastAPI (Uvicorn)** on port `8000`

Then visit 👉 [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 🧠 Main Endpoints

| Method | Endpoint | Description |
|--------|-----------|-------------|
| `POST` | `/auth/register` | Register new user |
| `POST` | `/auth/login` | Login and get JWT |
| `GET` | `/tasks/` | List tasks |
| `POST` | `/tasks/` | Create new task |
| `PUT` | `/tasks/{id}` | Update task |
| `DELETE` | `/tasks/{id}` | Delete task |
| `GET` | `/calendar/events` | View IT calendar events |
| `POST` | `/calendar/events` | Add new calendar event |

---

### 🔒 Security

- Authentication via **JWT tokens**
- Secure password hashing with **bcrypt**
- Environment-based configuration

---

### 👨‍💻 Author

**Xavier Cedeño**  
Systems Analyst | DevOps & Full Stack Developer  
🚀 Passionate about innovation, automation, and continuous learning.  
📫 [LinkedIn](https://www.linkedin.com) | [GitHub](https://github.com/<your-username>)
