from fastapi import FastAPI, Depends

from uuid import UUID
from enum import Enum

from mimesis.schema import Field, Schema
from pydantic import BaseModel, EmailStr, Field
from fastapi_pagination import PaginationParams, Page
from fastapi_pagination.paginator import paginate
import segno

from config import Settings, get_settings


app = FastAPI()


_ = Field()

dummy_users = Schema(
    lambda: {
        'id': _('uuid'),
        'name': _('name'),
        'surname': _('surname'),
        'email': _('email'),
        'age': _('age')
    }
)


class WifiEnum(str, Enum):
    """
    Accepted Wifi security settings.
    """
    wep = 'wep'
    wpa = 'wpa'
    wpa2 = 'wpa2'


class Dummy(BaseModel):
    """
    Dummy Pydantic model.
    """
    id: UUID
    name: str
    surname: str
    email: EmailStr
    age: int


class QRCode(BaseModel):
    """
    QRCode post input model
    """
    ssid: str
    password: str = Field(..., min_length=8, max_length=64)
    security: WifiEnum


class QRCodeOut(QRCode):
    """
    Removing password
    """
    ssid: str
    security: WifiEnum


def qr(ssid: str, passwd: WifiEnum, sec: str):
    """
    Return a QRcod
    """
    pass


@app.get('/info')
async def info(settings: Settings = Depends(get_settings)):
    """
    Returning the environment variables.
    """
    return {
        'app_name': settings.app_name,
        'admin_email': settings.admin_email,
        'items_per_user': settings.items_per_user,
    }


@app.get('/dummy', response_model=Page[Dummy])
async def dummy(params: PaginationParams = Depends()):
    """
    Returning dummy endpoint
    """
    dummy_data = dummy_users.create(iterations=100)

    return paginate(dummy_data, params)


@app.post('/qrcode', response_model=QRCodeOut)
async def qrcode() -> QRCode:
    """
    Simple QRCode Wifi generator.
    """
    pass
