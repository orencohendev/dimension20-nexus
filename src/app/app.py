from fastapi import FastAPI
import uvicorn
from app.conf import settings

# import the routers
from app.handlers import health
from app.handlers import campaign_handlers
from app.handlers import episode_handler


app = FastAPI()

# include the routers
app.include_router(health.router)
app.include_router(campaign_handlers.router)
app.include_router(episode_handler.router)


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
