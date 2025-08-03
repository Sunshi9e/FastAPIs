from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# In-memory storage for contacts
contacts: Dict[str, dict] = {}

# Contact model
class Contact(BaseModel):
    name: str
    phone: str
    email: str

@app.post("/contacts/")
def create_contact(contact: Contact):
    if contact.name in contacts:
        return {"error": "Contact with this name already exists."}
    contacts[contact.name] = contact.dict()
    return {"message": "Contact added successfully."}


@app.get("/contacts/")
def get_contact(name: str = Query(..., description="Name of the contact to fetch")):
    contact = contacts.get(name)
    if not contact:
        return {"error": "Contact not found."}
    return {"contact": contact}



@app.post("/contacts/{name}")
def update_contact(
    name: str = Path(..., description="Name of the contact to update"),
    phone: str = Body(..., embed=True),
    email: str = Body(..., embed=True)
):
    if name not in contacts:
        return {"error": "Contact not found."}
    
    contacts[name].update({"phone": phone, "email": email})
    return {"message": "Contact updated successfully."}


@app.post("/contacts/{name}")
def update_contact(
    name: str = Path(..., description="The name of the contact to update"),
    phone: str = Body(None, embed=True),
    email: str = Body(None, embed=True)
):
    if name not in contacts:
        return {"error": "Contact not found."}

    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email

    return {"message": f"Contact '{name}' updated.", "contact": contacts[name]}
