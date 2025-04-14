from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/slack/events")
async def slack_events(request: Request):
    data = await request.json()
    return {"challenge": data["challenge"]}
