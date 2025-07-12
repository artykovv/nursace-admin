import httpx
from fastapi import Request
from config.config import site_url_and_port


async def validate_token(token: str) -> int:
    url = f"{site_url_and_port}/auth/validate-token"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        return response.status_code


async def get_user_id_by_token(request: Request):
    token = request.cookies.get("Bearer")
    
    if not token:
        return None

    url = f"{site_url_and_port}/user/me"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get("id")
        return None