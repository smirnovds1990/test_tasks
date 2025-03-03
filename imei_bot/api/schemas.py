from pydantic import BaseModel


class IMEICheckRequestModel(BaseModel):
    """This is the wanted data form from a telegram user to check his IMEI."""
    imei: str
    token: str
