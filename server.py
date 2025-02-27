from fastapi import FastAPI

app = FastAPI()

# Biến lưu nội dung embed mới nhất cho từng boss
latest_doughking = {
    "status": "Offline",
    "data": {
        "playerCount": "None",
        "jobId": "None",
        "bossName": "None"
    }
}

latest_ripidra = {
    "status": "Offline",
    "data": {
        "playerCount": "None",
        "jobId": "None",
        "bossName": "None"
    }
}

latest_mirage = {
    "status": "Offline",
    "data": {
        "playerCount": "None",
        "jobId": "None",
        "time": "None"
    }
}

@app.get("/doughkingv2")
def get_doughking():
    return latest_doughking

@app.post("/doughkingv2")
def update_doughking(data: dict):
    global latest_doughking
    latest_doughking = {
        "status": "success" if data else "Offline",
        "data": {
            "playerCount": data.get("playerCount", "None"),
            "jobId": data.get("jobId", "None"),
            "bossName": data.get("bossName", "None")
        }
    }
    return {"message": "successful"}

@app.get("/ripindrav2")
def get_ripidra():
    return latest_ripidra

@app.post("/ripindrav2")
def update_ripidra(data: dict):
    global latest_ripidra
    latest_ripidra = {
        "status": "success" if data else "Offline",
        "data": {
            "playerCount": data.get("playerCount", "None"),
            "jobId": data.get("jobId", "None"),
            "bossName": data.get("bossName", "None")
        }
    }
    return {"message": "successful"}

@app.get("/mirage")
def get_mirage():
    return latest_mirage

@app.post("/mirage")
def update_mirage(data: dict):
    global latest_mirage
    latest_mirage = {
        "status": "success" if data else "Offline",
        "data": {
            "playerCount": data.get("playerCount", "None"),
            "jobId": data.get("jobId", "None"),
            "time": data.get("bossName", "None")
        }
    }
    return {"message": "successful"}
