import os
import requests
from io import BytesIO
from PIL import Image
from fastapi import APIRouter, Request
from grounded_sam_demo import gsam_main

router = APIRouter()

@router.post("/mask")
async def mask(request: Request):
    data = await request.json()

    config_file = "GroundingDINO/groundingdino/config/GroundingDINO_SwinT_OGC.py"
    grounded_checkpoint = "groundingdino_swint_ogc.pth"
    sam_checkpoint = "/content/sam_vit_h_4b8939.pth"
    image_path = data.get('image_path')
    output_dir = data.get('output_dir')
    box_threshold = 0.3
    text_threshold = 0.25
    text_prompt = data.get('text_prompt')
    device  = "cuda"

    print("[START] masking process")
    num_masks_detected = gsam_main(config_file, grounded_checkpoint, sam_checkpoint, image_path, output_dir, box_threshold, text_threshold, text_prompt, device)
    print("[END] masking process")

    return {"statusCode": 200, "num_mask_detected": num_masks_detected}