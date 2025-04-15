import uvicorn
from fastapi import FastAPI, Request
from pyngrok import ngrok

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/slack/events")
async def slack_events(request: Request):
    data = await request.json()
    event_type = data.get("type")

    if event_type == "event_callback":
        print(data)
        return {"status": "ok"}

    if event_type == "url_verification":
        return {"challenge": data["challenge"]}


if __name__ == "__main__":
    port = 8000
    http_tunnel = ngrok.connect(addr=f"{port}", bind_tls=True)
    print(f"ngrok url: {http_tunnel}")
    uvicorn.run("main:app", port=port)
