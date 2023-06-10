from pydantic import BaseModel


class Music_post_trade(BaseModel):
    price: int
    type: str
    name: str
    photo: str