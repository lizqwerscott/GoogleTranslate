import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from tran import google

class TranslateInput(BaseModel):
    data: str
    dest: str

app = FastAPI()


@app.post("/translate/google")
async def google_translate(item: TranslateInput):
    response = google.translate(item.data, item.dest)
    return response


if __name__ == '__main__':
    uvicorn.run(app='main:app', host="0.0.0.0", port=7777)
