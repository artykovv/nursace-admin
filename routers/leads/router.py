from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from config.token import validate_token
from dependencies.auth import get_auth_status
from config.config import site_url_and_port
from config.token import get_user_id_by_token

router = APIRouter(prefix="/leads")
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def leads_root(
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
        "leads/index.html",
        {
            "request": request,
            "is_authenticated": is_authenticated,
            "title": "Лиды",
            "site_url_and_port": site_url_and_port,
            "user_id": user_id,
            "current_page": "leads"
        }
    )

@router.get("/{lead_id}", response_class=HTMLResponse)
async def lead_detail(
    request: Request,
    lead_id: int,
    is_authenticated: bool = Depends(get_auth_status),
    user_id: str = Depends(get_user_id_by_token)
):
    if not is_authenticated:
        token = request.cookies.get("Bearer")
        if token:
            return RedirectResponse(url="/403", status_code=303)
        return RedirectResponse(url="/auth/login", status_code=303)

    return templates.TemplateResponse(
        "leads/detail.html",
        {
            "request": request,
            "is_authenticated": is_authenticated,
            "title": f"Лид #{lead_id}",
            "site_url_and_port": site_url_and_port,
            "user_id": user_id,
            "current_page": "leads",
            "lead_id": lead_id
        }
    ) 