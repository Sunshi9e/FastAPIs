# FastAPI Projects Collection

This repository contains multiple beginner-friendly projects built using **FastAPI** to practice and demonstrate various concepts such as path/query/body parameters, file handling, and state management using Python basics.

Each folder is a self-contained API project with its own `README.md`, requirements, and documentation.

---

## 📁 Projects Included

### 1. **Student Result Management API**
> Add students, calculate grades, and manage their results using a JSON-based backend.

- Adds subject scores per student
- Auto-calculates average and grade
- Prevents duplicate entries
- Stores data in `students.json`

---

### 2. **Mini Shopping API with Cart**
> Simulates a basic shopping experience with a simple cart system.

- View products
- Add to cart using query parameters
- Checkout with total cost (rounded)
- Cart saved to `cart.json`

---

### 3. **Job Application Tracker API**
> Track job applications with statuses like `pending`, `interview`, etc.

- Create, view, and search applications
- Stores data in `applications.json`
- Clean file handling via helper module

---

### 4. **Notes App API**
> Create, read, update, and delete notes as `.txt` files.

- File system-based note management
- Handles both overwrite and append operations
- Uses `os` module and error handling

---

### 5. **Simple Contact API**
> Basic CRUD-style contact management using only path and query parameters.

- In-memory contact storage
- Search, update, and add contacts
- Great for learning query/path param usage

---

## Getting Started

To run any of the APIs:

1. Navigate to the specific project folder:
   ```bash
   cd project_folder_name
   ```
2. Create and activate a virtual environment (optional but recommended):
    ```
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install dependencies:
    ```
    pip install fastapi uvicorn
    ```
4. Start the API:
    ```
    uvicorn main:app --reload
    ```
5. Visit the interactive docs at:
    ```
    http://127.0.0.1:8000/docs
    ```
##  Why This Repo? 💡

This project was built to:

- Reinforce core Python concepts

 - Practice FastAPI routing (path/query/body)

- Apply file handling and basic validation

- Learn version control with Git + GitHub

- Each task builds upon earlier skills with increasing complexity — ideal for learners transitioning from Python basics to API development.

## Tip

Check the individual README.md files inside each project folder for details like endpoint usage, data formats, and examples.

