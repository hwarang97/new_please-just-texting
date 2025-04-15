import uvicorn
from fastapi import BackgroundTasks, FastAPI, Request
from pyngrok import ngrok

from tasks.event_handler import handle_event_creation

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/slack/events")
async def slack_events(request: Request, background_task: BackgroundTasks):
    data = await request.json()
    event_type = data.get("type")

    if event_type == "event_callback":
        background_task.add_task(handle_event_creation, data)
        return {"status": "ok"}

    if event_type == "url_verification":
        return {"challenge": data["challenge"]}


if __name__ == "__main__":
    port = 8000
    http_tunnel = ngrok.connect(addr=f"{port}", bind_tls=True)
    print(f"ngrok url: {http_tunnel}")
    uvicorn.run("main:app", port=port)
