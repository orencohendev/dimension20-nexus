from fastapi import FastAPI
import uvicorn
from app.conf import config

# import the routers
from app.handlers import health
from app.handlers import campaign_handlers


app = FastAPI()

# include the routers
app.include_router(health.router)
app.include_router(campaign_handlers.router)



# run the app
if __name__ == "__main__":
    uvicorn.run(
        app="app.app:app",
        reload=config.is_dev,
        reload_dirs=["app"],
        host="0.0.0.0",
        loop="auto",
        port=config.service_port,
    )
