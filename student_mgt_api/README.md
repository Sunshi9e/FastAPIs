# Student Result Management API

A simple FastAPI-based project to manage student results — add scores, calculate grades, and retrieve student records.

##  Features

- Add student results with subject scores
- Automatically calculates average and assigns a grade
- Prevents duplicate student entries by name
- Retrieve a single student's result by name
- Retrieve all student records
- Saves data in a `students.json` file
- Basic error handling using `try-except`

##  Requirements 📦

- Python 3.7+
- FastAPI
- Uvicorn

## Installation & Running the API 🛠️ 

1. **Clone the project** (or create your own directory and `main.py`)

2. **Install dependencies**:
   ```bash
   pip install fastapi uvicorn
   ```


3. **Run the app**:
    ```bash
    uvicorn main:app --reload
    ```

4. **Test the endpoints using Postman or Swagger UI at:**
    ```bash
    http://127.0.0.1:8000/ENDPOINT
    ```

## API Endpoints 📚 

#### POST /students/

* Add a new student and calculate their grade.

* Request Body Example:

```bash
    {
    "name": "Alice",
    "subject_scores": {
        "math": 85,
        "english": 78,
        "science": 90
    }
    }
```

 #### GET /students/

- Returns all student records.

#### GET /students/{name}
- Fetch a single student's result by their name.