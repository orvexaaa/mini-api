from fastapi import FastAPI

app = FastAPI(title="mini API")

@app.get("/")
def home():
    return {
        "massage": "Mini API by orvexaa Is running!",
        "version" : "1.0.0",
        "status" : "success"
    }