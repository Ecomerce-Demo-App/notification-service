from fastapi import FastAPI

app = FastAPI()

@app.post("/notify")
def notify():

    return {
        "message": "Notification Sent"
    }
