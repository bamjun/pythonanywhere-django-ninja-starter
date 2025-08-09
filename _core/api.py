from ninja import NinjaAPI

from apis._router.health_router import health_router
from apis._router.triple_luck import triple_luck_router


api = NinjaAPI(
    title="pythonanywhere API",
    description="API for pythonanywhere",
    version="0.0.1",
)

api.add_router("/", health_router, tags=["health"])
api.add_router("/", triple_luck_router, tags=["triple_luck"])
