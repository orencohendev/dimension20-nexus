from fastapi.routing import APIRouter

router = APIRouter()


@router.get("/healthz")
async def healthz():
    """Health check endpoint. This endpoint is used to check if the service is up and running."""
    return {"status": "ok"}
