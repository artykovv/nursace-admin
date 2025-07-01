from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from config.token import validate_token
from dependencies.auth import get_auth_status
from config.config import site_url_and_port
from config.token import get_user_id_by_token

router = APIRouter(prefix="/products")
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def products_root(
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
        "products/index.html",
        {
            "request": request,
            "is_authenticated": is_authenticated,
            "title": "Товары",
            "site_url_and_port": site_url_and_port,
            "user_id": user_id,
            "current_page": "products"
        }
    )

@router.get("/{product_id}", response_class=HTMLResponse)
async def product_detail(
    product_id: int,
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
        "products/detail.html",
        {
            "request": request,
            "is_authenticated": is_authenticated,
            "title": f"Товар #{product_id}",
            "site_url_and_port": site_url_and_port,
            "user_id": user_id,
            "current_page": "products",
            "product_id": product_id
        }
    )

@router.get("/{product_id}/info", response_class=HTMLResponse)
async def product_update_info(
    product_id: int,
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
        "products/update_info.html",
        {
            "request": request,
            "is_authenticated": is_authenticated,
            "title": f"Изменить товар #{product_id}",
            "site_url_and_port": site_url_and_port,
            "user_id": user_id,
            "current_page": "products",
            "product_id": product_id,
            "token": request.cookies.get("Bearer")
        }
    )

@router.get("/{product_id}/image", response_class=HTMLResponse)
async def product_update_image(
    product_id: int,
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
        "products/update_image.html",
        {
            "request": request,
            "is_authenticated": is_authenticated,
            "title": f"Изменить изображения товара #{product_id}",
            "site_url_and_port": site_url_and_port,
            "user_id": user_id,
            "current_page": "products",
            "product_id": product_id,
            "token": request.cookies.get("Bearer")
        }
    ) 