from fastapi import FastAPI

app = FastAPI()

# Biến lưu nội dung embed mới nhất cho từng boss
latest_doughking = {"content": "None", "name boss": "None"}
latest_ripidra = {"content": "None", "name boss": "None"}

@app.get("/doughking")
def get_doughking():
    """Trả về nội dung embed mới nhất của Dough King"""
    return latest_doughking

@app.post("/doughking")
def update_doughking(data: dict):
    """Cập nhật nội dung embed của Dough King"""
    global latest_doughking
    latest_doughking = {
        "content": data.get("content", "None"),
        "name boss": data.get("name boss", "None")
    }
    return {"message": "successful"}

@app.get("/ripindra")
def get_ripidra():
    """Trả về nội dung embed mới nhất của Rip Indra"""
    return latest_ripidra

@app.post("/ripindra")
def update_ripidra(data: dict):
    """Cập nhật nội dung embed của Rip Indra"""
    global latest_ripidra
    latest_ripidra = {
        "content": data.get("content", "None"),
        "name boss": data.get("name boss", "None")
    }
    return {"message": "successful"}
