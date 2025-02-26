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

@app.get("/doughking")
def get_doughking():
    """Trả về dữ liệu mới nhất của Dough King"""
    return latest_doughking

@app.post("/doughking")
def update_doughking(data: dict):
    """Cập nhật dữ liệu của Dough King"""
    global latest_doughking
    latest_doughking = {
        "status": "Offline",
        "data": {
            "playerCount": data.get("playerCount", "None"),
            "jobId": data.get("content", "None"),
            "bossName": data.get("name_boss", "None")
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
        "status": "Offline",
        "data": {
            "playerCount": data.get("player_count", "None"),
            "jobId": data.get("content", "None"),
            "bossName": data.get("name_boss", "None")
        }
    }
    return {"message": "successful"}
