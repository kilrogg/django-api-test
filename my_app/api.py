from demo.api import api_v1

from .schema import ArtikelSchema


@api_v1.put("/artikel")
async def artikel(request, data: ArtikelSchema):
    return f"Data: {data}"

