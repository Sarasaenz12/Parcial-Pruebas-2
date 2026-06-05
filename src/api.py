from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.recarga import calcular_recarga, MontoInvalidoError

app = FastAPI(title="RecargaYa API")


class RecargaRequest(BaseModel):
    monto: float
    premium: bool = False


class RecargaResponse(BaseModel):
    monto: float
    bonificacion_pct: int


@app.post("/recarga", response_model=RecargaResponse)
def procesar_recarga(request: RecargaRequest):
    try:
        resultado = calcular_recarga(request.monto, request.premium)
        return resultado
    except MontoInvalidoError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/health")
def health():
    return {"status": "ok"}