import os
import requests
from io import BytesIO
from PIL import Image
from fastapi import APIRouter, Request
#from api.config import config
#from utils.smart_crop import crop_image   # Here I should load the main function from grounded_sam_demo

router = APIRouter()

@router.post("/mask")
async def mask(request: Request):
    data = await request.json()
    print(data)

    return {"message": "masking process started"}