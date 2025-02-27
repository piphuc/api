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

@app.get("/doughking")
def get_doughking():
    """Trả về dữ liệu mới nhất của Dough King"""
    return latest_doughking

@app.post("/doughking")
def update_doughking(data: dict):
    """Cập nhật dữ liệu của Dough King"""
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

@app.get("/ripindra")
def get_ripidra():
    """Trả về dữ liệu mới nhất của Rip Indra"""
    return latest_ripidra

@app.post("/ripindra")
def update_ripidra(data: dict):
    """Cập nhật dữ liệu của Rip Indra"""
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
    """Trả về dữ liệu mới nhất của Mirage"""
    return latest_mirage

@app.post("/mirage")
def update_mirage(data: dict):
    """Cập nhật dữ liệu của Mirage"""
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
