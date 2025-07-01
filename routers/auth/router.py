from fastapi import APIRouter, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from config.config import site_url_and_port

router = APIRouter(prefix="/auth")
templates = Jinja2Templates(directory="templates")

@router.get("/login", response_class=HTMLResponse)
async def base_root(request: Request):
    return templates.TemplateResponse(
        "auth/login.html",
        {
            "request": request,
            "site_url_and_port": site_url_and_port
        }
    )

@router.get("/logout")
async def page_(request: Request, response: Response):
    response = RedirectResponse(url="/")      
    response.delete_cookie("Bearer")
    return response