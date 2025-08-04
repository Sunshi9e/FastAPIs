# Simple Contact API with FastAPI 📇 

A lightweight contact management API built using **FastAPI**, designed to demonstrate how to use **path** and **query** parameters effectively.

---

## Features

- Add new contacts
- Get contacts by name (via query parameter)
- Update contact details using path + body parameters
- Input validation and basic error handling
- In-memory storage using Python dictionary

---

## Tech Stack 
Python 3.8+

FastAPI

Uvicorn (ASGI Server)


##  Contact Model 📦

Each contact has:

- `name`: string  
- `phone`: string  
- `email`: string  

Example:
```json
{
  "name": "Alice",
  "phone": "123-456-7890",
  "email": "alice@example.com"
}
```
## 📂 Endpoints

### ➕ Add a new contact
- POST /contacts/

- Body:

```json
{
  "name": "Alice",
  "phone": "123-456-7890",
  "email": "alice@example.com"
}
```
- Response:
```json
{
  "message": "Contact added successfully"
}
```

---
### 🔍 Get a contact by name

- GET /contacts/?name=Alice

- Response:
```json
{
  "name": "Alice",
  "phone": "123-456-7890",
  "email": "alice@example.com"
}
```
---
###  Update contact (path + body) ♻️

- POST /contacts/{name}

- Update either phone, email, or both.

- Body (example - update email only):

```Json
{
  "email": "newalice@example.com"
}
```

- Response:


```json
{
  "message": "Contact 'Alice' updated.",
  "contact": {
    "phone": "123-456-7890",
    "email": "newalice@example.com"
  }
}
```


## How to Run Locally ⚙️ 

1.  **Clone or create the folder and files:**
2. Create virtual environment (optional but recommended)
    ```python
    python -m venv venv
    ```
    ```
    source venv/bin/activate  # On Windows: 
    venv\Scripts\activate
    ```
3. Install dependencies
```
pip install fastapi uvicorn
```
4. Run the API
```
uvicorn main:app --reload
```
5. Visit Docs
Go to http://127.0.0.1:8000/docs to use the Swagger UI.


##  Notes
This API uses an in-memory dictionary to store contacts.

All data will be lost when the server restarts.

Ideal for learning purposes or small-scale prototypes.

