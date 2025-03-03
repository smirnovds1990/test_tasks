import httpx
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from constants import (
    API_ERROR_MESSAGE,
    AUTH_API_TOKEN,
    IMEICHECK_API_TOKEN,
    IMEICHECK_API_URL,
    IMEICHECK_SERVICE_ID,
)
from schemas import IMEICheckRequestModel


app = FastAPI()


@app.post("/api/check-imei")
async def check_imei(request: IMEICheckRequestModel):
    """Form a response according to validity of data from a user."""
    if request.token != AUTH_API_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")

    headers = {"Authorization": f"Bearer {IMEICHECK_API_TOKEN}"}
    imei_payload = {
        "deviceId": request.imei,
        "serviceId": IMEICHECK_SERVICE_ID,
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=IMEICHECK_API_URL,
            json=imei_payload,
            headers=headers,
        )
    if response.status_code == 201:
        return JSONResponse(content=response.json())
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail=API_ERROR_MESSAGE,
        )
