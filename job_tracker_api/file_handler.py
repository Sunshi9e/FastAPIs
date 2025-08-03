import json
import os

def load_applications():
    try:
        if os.path.exists("applications.json"):
            with open("applications.json", "r") as f:
                return json.load(f)
        else:
            return []
    except Exception as e:
        print("Error loading applications:", e)
        return []

def save_application(application_data):
    try:
        applications = load_applications()
        applications.append(application_data)

        with open("applications.json", "w") as f:
            json.dump(applications, f, indent=2)
    except Exception as e:
        print("Error saving application:", e)
