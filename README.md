# Todo_API

Una API RESTful desarrollada con **FastAPI** para gestionar tareas y usuarios. Esta API permite a los usuarios registrarse, iniciar sesión y realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre tareas, con autenticación mediante JWT y persistencia en PostgreSQL.

## 🚀 Características

- 🔐 **Autenticación** con JWT
- 👤 **Gestión de usuarios**: registro, login y perfil
- ✅ **CRUD de tareas** asociadas a usuarios
- 🗄️ **Base de datos PostgreSQL** usando SQLAlchemy
- 🐳 Soporte opcional para **Docker y Docker Compose**

---

## 📦 Requisitos previos

- Python 3.10 o superior  
- Docker y Docker Compose (opcional, recomendado para base de datos)

---

## ⚙️ Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/xJaider/Todo_API.git
   cd Todo_API
   ```

2. **Crea y activa un entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura las variables de entorno**:  
   Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:
   ```env
   DB_CONNECTION=postgresql
   POSTGRES_USER=root
   POSTGRES_PASSWORD=root
   POSTGRES_HOST=127.0.0.1
   POSTGRES_PORT=5432
   POSTGRES_DATABASE=todo_api_db
   PGADMIN_EMAIL=admin@ejemplo.com
   PGADMIN_PASSWORD=admin
   SECRET_KEY_TOKEN=tu_clave_secreta
   ```

5. **Inicia la base de datos (opcional con Docker)**:
   ```bash
   docker-compose up -d
   ```

6. **Inicializa las tablas de la base de datos**:
   ```bash
   python src/init_db.py
   ```

---

## ▶️ Ejecución

Lanza el servidor de desarrollo:

```bash
uvicorn src.main:app --reload
```

La API estará disponible en: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
Documentación automática en Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🔗 Endpoints principales

### Usuarios
- `POST /usuarios/` — Crear nuevo usuario  
- `GET /usuarios/me` — Obtener usuario autenticado

### Tareas
- `POST /tareas/` — Crear una tarea  
- `GET /tareas/` — Obtener todas las tareas  
- `GET /tareas/{id}` — Obtener tarea por ID  
- `PUT /tareas/{id}` — Actualizar tarea  
- `DELETE /tareas/{id}` — Eliminar tarea

### Autenticación
- `POST /login` — Iniciar sesión y obtener token JWT

---

## 🧪 Ejemplos de uso

### Crear un usuario
```bash
curl -X POST "http://127.0.0.1:8000/usuarios/" \
-H "Content-Type: application/json" \
-d '{
  "username": "usuario1",
  "email": "usuario1@ejemplo.com",
  "password": "password123"
}'
```

### Iniciar sesión
```bash
curl -X POST "http://127.0.0.1:8000/login" \
-H "Content-Type: application/json" \
-d '{
  "email": "usuario1@ejemplo.com",
  "password": "password123"
}'
```

### Crear una tarea
```bash
curl -X POST "http://127.0.0.1:8000/tareas/" \
-H "Authorization: Bearer <tu_token>" \
-H "Content-Type: application/json" \
-d '{
  "titulo": "Mi primera tarea",
  "descripcion": "Descripción de la tarea",
  "estado": "pendiente",
  "fecha_vencimiento": "2025-05-10"
}'
```

---

## 📁 Estructura del proyecto

```
todo_api/
├── src/
│   ├── auth.py
│   ├── crud/
│   ├── database.py
│   ├── init_db.py
│   ├── main.py
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   └── utils.py
├── docs/
├── .env
├── .gitignore
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas!  
Abre un *issue* o un *pull request* para sugerencias, mejoras o corrección de errores.

---

## 📝 Licencia

Este proyecto está bajo la licencia **MIT**. Consulta el archivo [LICENSE](LICENSE) para más información.
