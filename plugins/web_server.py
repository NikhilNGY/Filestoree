# plugins/web_server.py
# (©) Codexbotz

from aiohttp import web
import logging
from datetime import datetime

# Configure logger
logger = logging.getLogger("web_server")
logger.setLevel(logging.INFO)


# 🔹 Middleware to log each request
@web.middleware
async def logging_middleware(request, handler):
    try:
        response = await handler(request)
    except web.HTTPException as ex:
        logger.warning(f"{request.method} {request.path} -> {ex.status}")
        raise
    except Exception as e:
        logger.error(f"Error handling {request.method} {request.path}: {e}")
        raise
    else:
        logger.info(f"{request.method} {request.path} -> {response.status}")
        return response


# 🔹 Health-check route
async def health_check(request: web.Request) -> web.Response:
    return web.json_response(
        {
            "status": "ok",
            "service": "Telegram Bot",
            "timestamp": datetime.utcnow().isoformat() + "Z",
        }
    )


# 🔹 Home route
async def home(request: web.Request) -> web.Response:
    return web.Response(
        text="<h1>🚀 Bot Web Server is Running!</h1><p>Made by <a href='https://t.me/CodeXBotz'>CodeXBotz</a></p>",
        content_type="text/html",
    )


# 🔹 Example API route
async def echo(request: web.Request) -> web.Response:
    try:
        data = await request.json()
    except Exception:
        data = {"error": "Invalid JSON"}
    return web.json_response({"received": data})


# 🔹 Create aiohttp app
async def web_server() -> web.Application:
    app = web.Application(middlewares=[logging_middleware])
    app.add_routes(
        [
            web.get("/", home),
            web.get("/health", health_check),
            web.post("/echo", echo),
        ]
    )
    return app
