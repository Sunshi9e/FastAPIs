from fastapi import FastAPI
from pydantic import BaseModel
import file_handler

app = FastAPI()

class JobApplication(BaseModel):
    name: str
    company: str
    position: str
    status: str  

@app.post("/applications/")
def create_application(application: JobApplication):
    try:
        data = {
            "name": application.name,
            "company": application.company,
            "position": application.position,
            "status": application.status
        }

        file_handler.save_application(data)
        return {"message": "Application saved successfully", "application": data}
    except Exception as e:
        return {"error": str(e)}
    

@app.get("/applications/")
def get_all_applications():
    try:
        applications = file_handler.load_applications()
        return {"applications": applications}
    except Exception as e:
        return {"error": str(e)}


@app.get("/applications/search")
def search_applications(status: str):
    try:
        applications = file_handler.load_applications()
        matching = []

        for app in applications:
            if app["status"].lower() == status.lower():
                matching.append(app)

        return {"results": matching}
    except Exception as e:
        return {"error": str(e)}
