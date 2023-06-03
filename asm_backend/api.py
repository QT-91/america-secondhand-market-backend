import orjson
import decimal

from ninja.renderers import BaseRenderer
from ninja import NinjaAPI

from product.api import product_router


# api rendering (한글이 깨지는 문제) 
class ORJSONRenderer(BaseRenderer):
    media_type = "application/json"

    def render(self, request, data, *, response_status):
        def default(obj):
            if isinstance(obj, decimal.Decimal):
                return float(obj)
            raise TypeError

        return orjson.dumps(data, default=default)


api = NinjaAPI(renderer=ORJSONRenderer())


# add_routers
api.add_router('/product/', product_router)
