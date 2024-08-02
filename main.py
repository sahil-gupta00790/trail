from fastapi import FastAPI, File, UploadFile 
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
import base64

from pathlib import Path
import shutil




app = FastAPI()

class VideoData(BaseModel):
    videoContent: str
    fileType: str


@app.post("/acm/cctv")
async def upload_video(video: UploadFile = File(...)):
    try:
        # Create a temporary file to store the video
        with open(f"{video.filename}", "wb") as buffer:
            shutil.copyfileobj(video.file, buffer)
        
        # Here you can process the video file as needed
        # For example, you might want to move it to a permanent location
        # or perform some operations on it

        return JSONResponse(content={"message": "Video uploaded successfully"}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"message": f"An error occurred: {str(e)}"}, status_code=500)
    finally:
        video.file.close()



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)