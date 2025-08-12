from fastapi import APIRouter
from .main.router import router as main
from .auth.router import router as auth
from .leads.router import router as leads
from .orders.router import router as orders
from .products.router import router as products
from .clients.router import router as clients
from .report.router import router as report
from .site.router import router as site
from .settings.router import router as settings

routers = APIRouter()

routers.include_router(main)
routers.include_router(auth)
routers.include_router(leads)
routers.include_router(orders)
routers.include_router(products)
routers.include_router(clients)
routers.include_router(report)
routers.include_router(site)
routers.include_router(settings)