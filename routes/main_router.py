from fastapi import APIRouter

router = APIRouter(tags=['main'])


@router.get("/", include_in_schema=False)
async def root():
    return {"message": "Hello World"}
