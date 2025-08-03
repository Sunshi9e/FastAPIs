# Notes App API with FastAPI 📝 

A beginner-friendly FastAPI application to create, read, update, and delete notes as `.txt` files stored in the filesystem.

## Features

- Add new notes
- Read existing notes
- Update or append to notes
- Delete notes
- Stores notes as text files
- Basic error handling using try-except
- Uses `os` module for file system operations

## File Structure 📁 
```
notes_app/
├── main.py
├── notes/
│ └── [your_notes].txt
└── README.md
```

##  Requirements 📦

- Python 3.7+
- FastAPI
- Uvicorn

Install dependencies:

```bash
pip install fastapi uvicorn
```
##  Run the App 🏃‍♂️
```
uvicorn main:app --reload
```
- Visit: http://127.0.0.1:8000/docs for Swagger UI.

## Endpoints 📬 

| Method | Path             | Description                |
| ------ | ---------------- | -------------------------- |
| POST   | `/notes/`        | Create a new note          |
| GET    | `/notes/{title}` | Read a note by title       |
| POST   | `/notes/{title}` | Update or append to a note |
| DELETE | `/notes/{title}` | Delete a note              |

## Example Request Body
For creating a note:
```
{
  "title": "my_first_note",
  "content": "This is my first note."
}
```

## 📄 Notes
- All notes are saved as .txt files under the notes/ directory.

- Make sure the notes folder exists (it’s auto-created on first run).

- App uses basic error handling and os module, ideal for FastAPI beginners.