from fastapi import FastAPI, UploadFile
import uvicorn

app = FastAPI()

@app.put("/acm/cctv")
async def upload_video(file: UploadFile = UploadFile(...)):
    with open(file.filename, "wb") as f:
        f.write(await file.read())
    return {"message": "Video uploaded successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)