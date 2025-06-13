from fastapi import FastAPI 
from routes.user import user_router 
from routes.event import event_router
from routes.registration import registration_router
from routes.speaker import speaker_router


app = FastAPI()

app.include_router(user_router, prefix = "/user", tags=["Users"])
app.include_router(event_router, prefix = "/event", tags=["Events"])
app.include_router(registration_router, prefix = "/registration", tags=["Registration"])
app.include_router(speaker_router, prefix = "/speaker", tags=["Speakers"])

@app.get("/")
def home():
    return {"message": "Event Planning APP"}