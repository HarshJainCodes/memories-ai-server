from fastapi import APIRouter

router = APIRouter()


@router.get("/upload")
def upload_router():
	print("request to upload endpoint appeared")

	return "this is the upload router v2"
