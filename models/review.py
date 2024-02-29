#!/usr/bin/python3
"""Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
