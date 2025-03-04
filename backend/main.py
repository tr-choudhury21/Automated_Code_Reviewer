from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.review import review_code

app = FastAPI()

# Define request body format
class CodeReviewRequest(BaseModel):
    code: str

@app.get("/")
def home():
    return {"message": "Welcome to the Automated Code Reviewer API"}

@app.post("/review/")
def review_endpoint(request: CodeReviewRequest):
    try:
        result = review_code(request.code)
        return {"review": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
