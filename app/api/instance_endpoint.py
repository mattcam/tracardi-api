from fastapi import APIRouter, Depends
from fastapi import HTTPException

from app.api.auth.authentication import get_current_user
from tracardi.service.storage.driver import storage

router = APIRouter(
    dependencies=[Depends(get_current_user)]
)


@router.get("/instances", tags=["api-instance"])
async def all_api_instances():
    try:
        result = await storage.driver.api_instance.load_all()
        return {
            "total": result.total,
            "result": list(result)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/instances/stale", tags=["api-instance"])
async def remove_stale_api_instances():
    # todo remove stale instances
    pass
