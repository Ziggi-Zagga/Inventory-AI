# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import spacy

# Modelo de datos esperado
class InterpretRequest(BaseModel):
    text: str

# Iniciar FastAPI
app = FastAPI()

# Configurar CORS (ajusta en producción)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia esto si lo usas en producción
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cargar el modelo spaCy entrenado
nlp = spacy.load("inventory_model")

# Endpoint de prueba
@app.get("/")
async def root():
    return {"message": "🧠 Inventory AI Model is running."}

# Endpoint principal para interpretar frases
@app.post("/interpret")
async def interpret(request: InterpretRequest):
    doc = nlp(request.text)

    # Obtener intención más probable
    intent = max(doc.cats, key=doc.cats.get) if doc.cats else "unknown"

    # Obtener entidades
    entities = [{"entity": ent.label_, "text": ent.text} for ent in doc.ents]

    # Devolver todo (incluye la frase original como pediste)
    return {
        "original_text": request.text,
        "intent": intent,
        "entities": entities
    }
