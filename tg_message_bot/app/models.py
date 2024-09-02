from pydantic import BaseModel, BeforeValidator, Field
from typing import Annotated, List, Optional


PyObjectId = Annotated[str, BeforeValidator(str)]


class BaseMessage(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    text: str
    author: str


class MessagesList(BaseModel):
    messages: List[BaseMessage]
