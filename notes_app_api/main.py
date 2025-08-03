from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()


NOTES_DIR = "notes"


if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)


class Note(BaseModel):
    title: str
    content: str

@app.post("/notes/")
def create_note(note: Note):
    try:
        file_path = os.path.join(NOTES_DIR, f"{note.title}.txt")
        if os.path.exists(file_path):
            return {"error": "Note already exists"}
        
        with open(file_path, "w") as f:
            f.write(note.content)
        
        return {"message": f"Note '{note.title}' created successfully."}
    
    except Exception as e:
        return {"error": str(e)}
