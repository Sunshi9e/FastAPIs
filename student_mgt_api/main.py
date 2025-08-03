from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
import json
import os

app = FastAPI()

class Student(BaseModel):
    name: str
    subject_scores: Dict[str, float]


def save_student(student_data):
    try:
        
        if os.path.exists("students.json"):
            with open("students.json", "r") as file:
                students = json.load(file)
        else:
            students = []

        students.append(student_data)

        with open("students.json", "w") as file:
            json.dump(students, file, indent=2)

    except Exception as e:
        print("Error saving student:", e)


@app.post("/students/")
def create_student(student: Student):
    try:
        students = load_students()

        # Check for duplicate name
        for existing_student in students:
            if existing_student["name"].lower() == student.name.lower():
                return {"error": f"Student with name '{student.name}' already exists"}

        scores = student.subject_scores
        average = sum(scores.values()) / len(scores)

        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
        elif average >= 60:
            grade = "D"
        else:
            grade = "F"

        student_data = {
            "name": student.name,
            "subject_scores": student.subject_scores,
            "average": average,
            "grade": grade
        }

        save_student(student_data)
        return {"message": "Student added successfully", "student": student_data}

    except Exception as e:
        return {"error": str(e)}


def load_students():
    try:
        if os.path.exists("students.json"):
            with open("students.json", "r") as file:
                return json.load(file)
        else:
            return []
    except Exception as e:
        print("Error loading students:", e)
        return []


@app.get("/students/{name}")
def get_student(name: str):
    try:
        students = load_students()
        for student in students:
            if student["name"].lower() == name.lower():
                return {"student": student}
        return {"message": "Student not found"}
    except Exception as e:
        return {"error": str(e)}


@app.get("/students/")
def get_all_students():
    try:
        students = load_students()
        return {"students": students}
    except Exception as e:
        return {"error": str(e)}



@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Result Management API!"}