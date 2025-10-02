# DocentIA-App
**Asistente personal de estudio**: genera exámenes y tests de prueba, y ofrece correcciones personalizadas.

>[!IMPORTANT]
>Este es un proyecto creado por una estudiante para aprender a usar LLMs y a usar Python. ¡Cualquier tipo de ayuda es bienvenida!

## 🧩 To-Do List
### Producto mínimo viable
---
- **Entrada de datos**
    - [ ] Subida de documentos al programa
    - [x] Extracción del texto del PDF
    - [ ] Normalización y limpieza del texto 
    - [ ] Chunking/Splitter
    - [x] Embedding
    - [ ] Subir embeddings a la base de datos
- **Generación de preguntas para el examen**
    - [ ] Generación de las preguntas según los contenidos dados por el usuario
- **Corrección y feedback**
    - [ ] Nota general
    - [ ] Preguntas falladas y su justificación
- **Funcionamiento general**
    - [ ] Botón de bugs, conectividad con el mail
### Extras
---
- [ ] Generar opciones para la creación de preguntas (tipo escrito, test, mixto, dificultad, largo, cronómetro, opciones múltiples...)
- [ ] Interfaz (mascotas y themes!)
- [ ] Guardar el progreso en medio del examen
- [ ] Descargar exámenes sin hacer, con las respuestas del usuario corregidas, sin corregir, o hechos por la IA para repaso
- [ ] Gráficas de rendimiento
- [ ] Marcar zonas del PDF relacionadas con los fallos
- [ ] Compartir los exámenes
- [ ] Historial personal 


## 📁 Estructura del proyecto

    DocentIA-App/
    │
    ├── DocentIA                # Django project
    │   └── DocentIA_App        # Django Application
    │       └── migrations
    │       └── templates       # HTMLs
    │       └── urls.py
    │       └── views.py    
    │
    ├── src/                     
    │   └── __init__.py
    ├── tests/                     
    ├── docs/                     
    │   └── __init__.py
    │
    ├── .gitignore
    ├── .env
    ├── README.md
    ├── requirements.txt        # Python dependencies
    └── main.py                 # Main script

## 🧰 Tech Stack

- Python 3.11.9
. Django 5.2.6
- LangChain
- Pydantic
- MongoDB
- PyMuPDF

