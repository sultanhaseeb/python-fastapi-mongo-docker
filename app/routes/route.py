from fastapi import APIRouter
from models.user import User  # Import the User model
from config.database import collection_name  # MongoDB collection
from schemas.schemas import (
    list_serial,
)  # Helper function to serialize MongoDB documents
from bson import ObjectId  # For working with MongoDB ObjectIDs

# Initialize FastAPI router for managing user-related API endpoints
router = APIRouter()


# GET all users from the database
@router.get("/")
async def get_users():
    # Retrieve all users and serialize them for the response
    users = list_serial(collection_name.find())  # Find all users
    return users  # Return the list of users


# POST (create) a new user in the database
@router.post("/")
async def post_user(user: User):
    # Insert the new user into the MongoDB collection
    collection_name.insert_one(dict(user))  # Convert Pydantic model to dict and insert


# PUT (update) an existing user by ID
@router.put("/{id}")
async def put_user(id: str, user: User):
    # Update the user document with the specified ID
    collection_name.find_one_and_update(
        {"_id": ObjectId(id)},  # Find the user by ObjectId
        {"$set": dict(user)},  # Update the document with the new data
    )


# DELETE a user by ID
@router.delete("/{id}")
async def delete_user(id: str):
    # Delete the user document with the specified ID
    collection_name.find_one_and_delete(
        {"_id": ObjectId(id)}
    )  # Remove the user by ObjectId
