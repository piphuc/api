from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Biến lưu dữ liệu mới nhất
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

# Định nghĩa dữ liệu đầu vào
class BossData(BaseModel):
    playerCount: str
    jobId: str
    bossName: str

@app.get("/doughking")
def get_doughking():
    """Trả về dữ liệu mới nhất của Dough King"""
    return latest_doughking

@app.post("/doughking")
def update_doughking(data: BossData):
    """Cập nhật dữ liệu của Dough King"""
    global latest_doughking
    latest_doughking = {
        "status": "success",
        "data": data.dict()  # Chuyển thành dictionary
    }
    return {"message": "successful"}

@app.get("/ripindra")
def get_ripidra():
    """Trả về dữ liệu mới nhất của Rip Indra"""
    return latest_ripidra

@app.post("/ripindra")
def update_ripidra(data: BossData):
    """Cập nhật dữ liệu của Rip Indra"""
    global latest_ripidra
    latest_ripidra = {
        "status": "success",
        "data": data.dict()
    }
    return {"message": "successful"}
