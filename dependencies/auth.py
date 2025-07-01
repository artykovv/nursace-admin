# dependencies/auth.py

from fastapi import Request
from fastapi.responses import RedirectResponse
import httpx
from config.config import site_url_and_port

async def get_auth_status(request: Request) -> bool:
    token = request.cookies.get("Bearer")
    if not token:
        return False

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{site_url_and_port}/auth/admin-token",
                headers={"Authorization": f"Bearer {token}"}
            )
            return response.status_code == 200
    except Exception:
        return False