# 🧾 Job Application Tracker API

A beginner-friendly FastAPI project to manage and search job applications.  
This simple REST API allows you to add job applications, view all, and search by status.  
Built using Python basics and core FastAPI concepts — no advanced tricks, just clean logic.

---

## Features 📦 

- Add new job applications
- View all saved applications
- Filter/search applications by status (`pending`, `interview`, `rejected`, etc.)
- Saves all application data to `applications.json`
- Input validation using `try-except`
- Clean file handling logic in a separate `file_handler.py` module

---

## Technologies Used 🛠️ 

- Python 3.x
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/) (ASGI Server)
- Built-in `json` and `os` modules (no external dependencies)

---

##  Project Structure 📁

```
job-tracker/
├── main.py # Main FastAPI app
├── file_handler.py # Handles JSON file read/write
├── applications.json # Stores saved applications
└── README.md # Project documentation
```


---

##  How to Run ▶️

1.  **Clone or create the folder and files:**

2. **Install dependencies**
    ```
    pip install fastapi uvicorn
    ```
3. **Start the server**
    ```
    uvicorn main:app --reload
    ```
4. **Test the endpoints using Postman or Swagger UI at:**
    ```bash
    http://127.0.0.1:8000/ENDPOINT
    ```
    - where **"ENDPOINT"** should be the actual endpoints. 

##  API Endpoints 🔌


## Add a New Application ➕ 
- POST /applications/
- Add a job application using the request body. eg
```
{
  "name": "Victor Robin",
  "company": "OpenAI",
  "position": "Backend Developer",
  "status": "pending"
}
```

## Get All Applications 📄 
- GET /applications/
- Returns all saved job applications.

## Search Applications by Status 🔍 
- GET /applications/search?status=pending
- Returns all applications that match the specified  status.

## Data Format
- All applications are saved to applications.json like this:
```
[
  {
    "name": "Victor Robin",
    "company": "OpenAI",
    "position": "Backend Developer",
    "status": "pending"
  }
]
```
## ⭐️ Support
If you found this helpful, feel free to give a ⭐️ on GitHub!