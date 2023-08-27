# Fast Api server implementation, which receives files and transcribes them

from fastapi import FastAPI, UploadFile

# Fast API server. Add (docs_url=None, redoc_url=None) if you want to prevent
# accessing the docsumentation.
app = FastAPI()

# CORS configuration below, Uncomment if a web
# applications running at one origin to access resources
#  from a server at a different origin.
# from fastapi.middleware.cors import CORSMiddleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.get("/")
def read_root():
    return {"Hello": "World"}


# Upload file api

@app.post("/uploadfile/")
async def receive_file(file: UploadFile, user_id: str):
    return {"file_uploaded": True}
