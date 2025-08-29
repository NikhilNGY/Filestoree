(©) Codexbotz

from aiohttp import web
import json
from datetime import datetime

# Simple health-check route
async def health_check(request: web.Request) -> web.Response:
    return web.json_response(
        {
            "status": "ok",
            "service": "Telegram Bot",
            "timestamp": datetime.utcnow().isoformat() + "Z",
        }
    )

# Example home route
async def home(request: web.Request) -> web.Response:
    return web.Response(
        text="<h1>🚀 Bot Web Server is Running!</h1><p>Made by <a href='https://t.me/CodeXBotz'>CodeXBotz</a></p>",
        content_type="text/html",
    )

# Example API endpoint
async def echo(request: web.Request) -> web.Response:
    try:
        data = await request.json()
    except Exception:
        data = {"error": "Invalid JSON"}
    return web.json_response({"received": data})


async def web_server() -> web.Application:
    """
    Creates and configures an aiohttp web application.
    This will be attached to the bot runner in bot.py
    """
    app = web.Application()
    app.add_routes(
        [
            web.get("/", home),
            web.get("/health", health_check),
            web.post("/echo", echo),
        ]
    )
    return app
