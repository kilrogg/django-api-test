from decimal import Decimal

from ninja import Schema

class ArtikelSchema(Schema):
    artikelnr: str
    bezeichnung: str
    artikelgruppen: list[str]
    merkmale: dict[str, str]
    dimensionen: dict[str, Decimal]
