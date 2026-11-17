from pathlib import Path
from typing import Annotated

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from app import servicios

app = FastAPI()
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")


class RespuestaRequest(BaseModel):
    id: int
    opcion: int = Field(ge=0, le=3)


@app.get("/")
def pagina_principal(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request},
    )


@app.get("/api/preguntas")
def listar_preguntas(
    cantidad: Annotated[int, Query(ge=1, le=5)] = 5,
):
    return servicios.obtener_preguntas(cantidad)


@app.post("/api/responder")
def responder(respuesta: RespuestaRequest):
    resultado = servicios.evaluar_respuesta(respuesta.id, respuesta.opcion)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")
    return resultado
