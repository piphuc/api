from fastapi import FastAPI

app = FastAPI()

# Biến lưu nội dung embed mới nhất
latest_embed = {"content": "Chưa có dữ liệu", "name boss": "Chưa có tên boss"}

@app.get("/embed")
def get_embed():
    """Trả về nội dung embed mới nhất"""
    return latest_embed

@app.post("/embed")
def update_embed(data: dict):
    """Cập nhật nội dung embed"""
    global latest_embed
    # Lấy giá trị của content và name boss từ dữ liệu nhận được
    latest_embed = {
        "content": data.get("content", "Không có dữ liệu"),
        "name boss": data.get("name boss", "Không có tên boss")  # Cập nhật name boss
    }
    return {"message": "Cập nhật thành công"}

