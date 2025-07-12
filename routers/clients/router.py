from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from dependencies.auth import get_auth_status
from config.config import site_url_and_port
from config.token import get_user_id_by_token

router = APIRouter(prefix="/clients")
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def clients_root(
    request: Request,
    is_authenticated: bool = Depends(get_auth_status),
    user_id: str = Depends(get_user_id_by_token)
):
    if not is_authenticated:
        token = request.cookies.get("Bearer")
        if token:
            return RedirectResponse(url="/403", status_code=303)
        return RedirectResponse(url="/auth/login", status_code=303)

    return templates.TemplateResponse(
        "clients/index.html",
        {
            "request": request,
            "is_authenticated": is_authenticated,
            "title": "Клиенты",
            "site_url_and_port": site_url_and_port,
            "user_id": user_id,
            "current_page": "clients"
        }
    )

@router.get('/clients/orders.html', response_class=HTMLResponse)
def client_orders_page(request: Request):
    return templates.TemplateResponse('clients/orders.html', {
        'request': request,
        "site_url_and_port": site_url_and_port,
    }) 