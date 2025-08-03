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

class NoteUpdate(BaseModel):
    content: str
    mode: str = "overwrite"


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
    

@app.get("/notes/{title}")
def read_note(title: str):
    try:
        file_path = os.path.join(NOTES_DIR, f"{title}.txt")
        if not os.path.exists(file_path):
            return {"error": "Note not found"}

        with open(file_path, "r") as f:
            content = f.read()
        
        return {"title": title, "content": content}
    
    except Exception as e:
        return {"error": str(e)}
    

@app.post("/notes/{title}")
def update_note(title: str, update: NoteUpdate):
    try:
        file_path = os.path.join(NOTES_DIR, f"{title}.txt")
        if not os.path.exists(file_path):
            return {"error": "Note not found"}

        if update.mode == "append":
            with open(file_path, "a") as f:
                f.write("\n" + update.content)
        else:  # overwrite
            with open(file_path, "w") as f:
                f.write(update.content)
        
        return {"message": f"Note '{title}' updated successfully in '{update.mode}' mode."}
    
    except Exception as e:
        return {"error": str(e)}


@app.delete("/notes/{title}")
def delete_note(title: str):
    try:
        file_path = os.path.join(NOTES_DIR, f"{title}.txt")
        if not os.path.exists(file_path):
            return {"error": "Note not found"}

        os.remove(file_path)
        return {"message": f"Note '{title}' deleted successfully."}
    
    except Exception as e:
        return {"error": str(e)}
