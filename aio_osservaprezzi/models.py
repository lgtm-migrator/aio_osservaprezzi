"""Models for aio_osservaprezzi."""

import attr
from typing import Optional, Dict

@attr.s(auto_attribs=True, frozen=True)
class Fuel:
    name : str
    id: str
    is_self : bool
    price: float

    @staticmethod
    def from_dict(data):
        return Fuel(
            name = data['carb'],
            id = data['idCarb'],
            is_self = bool(data['isSelf']),
            price = data['prezzo'],
        )

@attr.s(auto_attribs=True, frozen=True)
class Station:
    name: str
    latitude: str
    longitude: str
    id: int
    bnd: str
    addr: str
    fuels: Dict[Fuel, None]
    update: str

    @staticmethod
    def from_dict(data):
        
        return Station(
            name = data['name'],
            latitude = data['lat'],
            longitude = data['lon'],
            id = data['id'],
            bnd = data['bnd'],
            addr = data['addr'],
            fuels = [Fuel.from_dict(k) for k in data["carburanti"]],
            update = data['dIns']
            # 2020-08-08 08:36:09
        )

