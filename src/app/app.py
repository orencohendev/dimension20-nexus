from fastapi import FastAPI
from pathlib import Path
from fastapi.staticfiles import StaticFiles
import uvicorn
from app.conf import settings

# import the routers
from app.handlers import health
from app.handlers import campaign_handlers
from app.handlers import episode_handler


app = FastAPI(
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

build_dir = Path(__file__).parent / "frontend_build" / "build"
app.mount("/assets", StaticFiles(directory=f"{build_dir}/assets"), name="assets")

# include the routers
app.include_router(health.router)
app.include_router(campaign_handlers.router, prefix="/api")
app.include_router(episode_handler.router, prefix="/api")


@app.get("/{full_path:path}")
async def serve_react_app(full_path: str):
    index_file = Path(f"{build_dir}/index.html")
    if index_file.exists():
        return await StaticFiles(directory=str(build_dir)).get_response(
            "index.html", {"method": "GET", "headers": {}}
        )
    return {"message": "No build found"}


# run the app
if __name__ == "__main__":

    uvicorn.run(
        app="app.app:app",
        reload=settings.is_dev,
        reload_dirs=["app"],
        host="0.0.0.0",
        loop="auto",
        port=settings.service_port,
    )
