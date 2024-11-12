import os
import json
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Usuario(BaseModel):
    nombre: str
    edad: int
    profesion: str

DIRECTORIO = "/mnt/c/Users/jose/Documentos/datos_usuarios"

os.makedirs(DIRECTORIO, exist_ok=True)

@app.post("/usuario/")
async def crear_usuario(user_data: Usuario):
    datos_usuario = user_data.dict()
    
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    nombre_archivo = f"{DIRECTORIO}/usuario_{timestamp}.json"
    
    with open(nombre_archivo, "w") as archivo:
        json.dump(datos_usuario, archivo)
    
    return {"mensaje": "Usuario creado y almacenado en archivo JSON", "archivo": nombre_archivo}
