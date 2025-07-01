from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from config.token import validate_token
from dependencies.auth import get_auth_status
from config.config import site_url_and_port
from config.token import get_user_id_by_token

router = APIRouter(prefix="/site")
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def site_root(
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
        "site/index.html",
        {
            "request": request,
            "is_authenticated": is_authenticated,
            "title": "Сайт",
            "site_url_and_port": site_url_and_port,
            "user_id": user_id,
            "current_page": "site"
        }
    ) 

@router.get("/banner", response_class=HTMLResponse)
async def site_banner(
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
        "site/banner.html",
        {
            "request": request,
            "is_authenticated": is_authenticated,
            "title": "Баннер",
            "site_url_and_port": site_url_and_port,
            "user_id": user_id,
            "current_page": "site",
            "current_mini_page": "banner"
        }
    ) 

@router.get("/banner/update", response_class=HTMLResponse)
async def banner_update(
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
        "site/banner_update.html",
        {
            "request": request,
            "is_authenticated": is_authenticated,
            "title": "Изменить баннер",
            "site_url_and_port": site_url_and_port,
            "user_id": user_id,
            "current_page": "site",
            "current_mini_page": "banner"
        }
    )

@router.get("/documents", response_class=HTMLResponse)
async def site_documents(
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
        "site/documents.html",
        {
            "request": request,
            "is_authenticated": is_authenticated,
            "title": "Документы",
            "site_url_and_port": site_url_and_port,
            "user_id": user_id,
            "current_page": "site",
            "current_mini_page": "documents"
        }
    )

@router.get("/documents/add", response_class=HTMLResponse)
async def documents_add(
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
        "site/documents_add.html",
        {
            "request": request,
            "is_authenticated": is_authenticated,
            "title": "Добавить документ",
            "site_url_and_port": site_url_and_port,
            "user_id": user_id,
            "current_page": "site",
            "current_mini_page": "documents"
        }
    )

@router.get("/documents/update/{doc_id}", response_class=HTMLResponse)
async def documents_update(
    request: Request,
    doc_id: int,
    is_authenticated: bool = Depends(get_auth_status),
    user_id: str = Depends(get_user_id_by_token)
):
    if not is_authenticated:
        token = request.cookies.get("Bearer")
        if token:
            return RedirectResponse(url="/403", status_code=303)
        return RedirectResponse(url="/auth/login", status_code=303)

    return templates.TemplateResponse(
        "site/documents_update.html",
        {
            "request": request,
            "is_authenticated": is_authenticated,
            "title": "Изменить документ",
            "site_url_and_port": site_url_and_port,
            "user_id": user_id,
            "current_page": "site",
            "current_mini_page": "documents",
            "doc_id": doc_id
        }
    )

@router.get("/categories", response_class=HTMLResponse)
async def site_categories(
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
        "site/categories.html",
        {
            "request": request,
            "is_authenticated": is_authenticated,
            "title": "Категории",
            "site_url_and_port": site_url_and_port,
            "user_id": user_id,
            "current_page": "site",
            "current_mini_page": "categories"
        }
    )

@router.get("/categories/add", response_class=HTMLResponse)
async def categories_add(
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
        "site/categories_add.html",
        {
            "request": request,
            "is_authenticated": is_authenticated,
            "title": "Добавить категорию",
            "site_url_and_port": site_url_and_port,
            "user_id": user_id,
            "current_page": "site",
            "current_mini_page": "categories"
        }
    )

@router.get("/pages", response_class=HTMLResponse)
async def site_pages(
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
        "site/pages.html",
        {
            "request": request,
            "is_authenticated": is_authenticated,
            "title": "Страницы",
            "site_url_and_port": site_url_and_port,
            "user_id": user_id,
            "current_page": "site",
            "current_mini_page": "pages"
        }
    )

@router.get("/categories/{category_id}/products", response_class=HTMLResponse)
async def categories_products(
    request: Request,
    category_id: int,
    is_authenticated: bool = Depends(get_auth_status),
    user_id: str = Depends(get_user_id_by_token)
):
    if not is_authenticated:
        token = request.cookies.get("Bearer")
        if token:
            return RedirectResponse(url="/403", status_code=303)
        return RedirectResponse(url="/auth/login", status_code=303)

    return templates.TemplateResponse(
        "site/categories_products.html",
        {
            "request": request,
            "is_authenticated": is_authenticated,
            "title": "Добавить товары в категорию",
            "site_url_and_port": site_url_and_port,
            "user_id": user_id,
            "current_page": "site",
            "current_mini_page": "categories",
            "category_id": category_id
        }
    ) 