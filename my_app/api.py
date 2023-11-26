from django.http import HttpRequest

from demo.api import api_v1

from .schema import ArtikelSchema


@api_v1.put("/artikel")
async def artikel(request: HttpRequest, data: ArtikelSchema) -> str:
    return f"Data: {data}"
