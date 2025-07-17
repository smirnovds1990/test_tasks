import os

from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile
from jigsawstack import JigsawStack

from constants import ALLOWED_NSFW_SCORE, OK_RESPONSE, REJECT_RESPONSE


load_dotenv()
app = FastAPI()
jigsaw = JigsawStack(api_key=os.getenv("API_KEY"))


@app.post("/moderate")
async def check_image_for_nsfw_content(
    image: UploadFile
) -> dict[str, str]:
    """
    Get an image and check if it contains nsfw content.

    Args:
        image: .jpg/.png file.

    Returns:
        {"status": "OK"}: if the image has no nsfw content.
        {"status": "REJECTED", "reason": "NSFW content"}: if the image has
        nsfw content.
    """
    response = jigsaw.validate.nsfw(await image.read())
    nsfw_score = response["nsfw_score"]
    if nsfw_score > ALLOWED_NSFW_SCORE:
        return REJECT_RESPONSE
    return OK_RESPONSE
