import pymongo
import datetime

import os
import dotenv
dotenv.load_dotenv()
DB_URL = os.getenv('DB_URL')

import json

client = pymongo.MongoClient(DB_URL)
db = client["fast_api_testing"]

from schema import *

def add_user(user: User):
    try:
        status = db['users'].insert_one({
            "_id" : user.id,
            'user_name': user.user_name,
            'email': user.email,
            'email_verified': user.email_verified,
            'password_hash': user.password_hash
        })
        return 200, {"success": True}
    except pymongo.errors.DuplicateKeyError:
        return 400, {"error" : "User already exists"}
    except Exception as E:
        return 400, {"error" : str(E)}

def add_staff(staff_inst : Staff):
    try:
        user = db["users"].find_one({"_id" : staff_inst.id})
        hotel = db["hotels"].find_one({"_id" : staff_inst.hotel_id})

        if user and hotel:
            status = db["staff"].insert_one({
                "_id" : staff_inst.id,
                "name" : staff_inst.name,
                "mobile" : staff_inst.mobile,
                "mobile_verified" : staff_inst.mobile_verified,
                "hotel_id" : staff_inst.hotel_id,
                "rating" : staff_inst.rating,
                "created_at": datetime.datetime.utcnow(),
                "updated_at": datetime.datetime.utcnow()            
            })
            return 200, {"success": True}
        else:
            return 400, {"error": "User or Hotel not found"}
    except pymongo.errors.DuplicateKeyError:
        return 400, {"error" : "Staff already exists"}
    except Exception as E:
        return 400, {"error" : str(E)}

def add_admin(admin_inst : Admin):
    try:
        user = db["users"].find_one({"_id" : admin_inst.id})

        if user:
            status = db["admins"].insert_one({
                "_id" : admin_inst.id,
                "name" : admin_inst.name,
                "mobile" : admin_inst.mobile,
                "mobile_verified" : admin_inst.mobile_verified,
                "dob" : admin_inst.dob,
                "active" : admin_inst.active,
                "created_at": datetime.datetime.utcnow(),
                "updated_at": datetime.datetime.utcnow()                      
            })
            return 200, {"success": True}
        else:
            return "User not found"
    except pymongo.errors.DuplicateKeyError:
        return 400, {"error" : "Admin already exists"}
    except Exception as E:
        return 400, {"error" : str(E)}

def add_customer(cust_inst : Customer):
    try:
        user = db["users"].find_one({"_id" : cust_inst.id})

        if user:
            status = db["customers"].insert_one({
                "_id" : cust_inst.id,
                "name" : cust_inst.name,
                "mobile" : cust_inst.mobile,
                "mobile_verified" : cust_inst.mobile_verified,
                "dob" : cust_inst.dob,
                "active" : cust_inst.active,
                "created_at": datetime.datetime.utcnow(),
                "updated_at": datetime.datetime.utcnow()                   
            })
            return 200, {"success": True}
        else:
            return "User not found"
    except pymongo.errors.DuplicateKeyError:
        return 400, {"error" : "Customer already exists"}
    except Exception as E:
        return 400, {"error" : str(E)}

def add_hotel(hotel_inst : Hotel):
    try:
        status = db["hotels"].insert_one({
            "_id" : hotel_inst.id,
            "name" : hotel_inst.name,
            "location" : hotel_inst.location,
            "state" : hotel_inst.state,
            "rating" : hotel_inst.rating,
            "image_link" : hotel_inst.image_link,
            "gym_available" : hotel_inst.gym_available,
            "food_available" : hotel_inst.food_available,
            "allows_booking" : hotel_inst.allows_booking
        })
        return 200, {"success": True}
    
    except pymongo.errors.DuplicateKeyError:
        return 400, {"error" : "Hotel already exists"}
    except Exception as E:
        return 400, {"error" : str(E)}

def add_room(room_inst : Room):
    try:
        hotel = db["hotels"].find_one({"_id" : room_inst.hotel_id})

        if hotel:
            status = db["rooms"].insert_one({
                "_id" : room_inst.id,
                "hotel_id" : room_inst.hotel_id,
                "room_type" : room_inst.room_type,
                "room_number" : room_inst.room_number,
                "price" : room_inst.price,
                "rating" : room_inst.rating,
                "image_link" : room_inst.image_link,
                "created_at": datetime.datetime.utcnow(),
                "updated_at": datetime.datetime.utcnow()      
            })
            return 200, {"success": True}
        else:
            return "Hotel not found"
    except pymongo.errors.DuplicateKeyError:
        return 400, {"error" : "Room already exists"}
    
    except Exception as E:
        return 400, {"error" : str(E)}

def add_booking(booking_inst : Booking):
    try:
        customer = db["customers"].find_one({"_id" : booking_inst.customer_id})
        room = db["rooms"].find_one({"_id" : booking_inst.room_id})

        if customer and room:
            status = db["bookings"].insert_one({
                "_id" : booking_inst.id,
                "customer_id" : booking_inst.customer_id,
                "room_id" : booking_inst.room_id,
                "check_in" : booking_inst.check_in,
                "check_out" : booking_inst.check_out,
                "booking_status" : booking_inst.booking_status,
                "total_price" : booking_inst.total_price
            })
            return 200, {"success": True}
        else:
            return "Customer or Room not found"
    except pymongo.errors.DuplicateKeyError:
        return 400, {"error" : "Booking already exists"}
    
    except Exception as E:
        return 400, {"error" : str(E)}

def add_payment(payment_inst : Payment):
    try:
        booking = db["bookings"].find_one({"_id" : payment_inst.booking_id})

        if booking:
            status = db["payments"].insert_one({
                "_id" : payment_inst.id,
                "booking_id" : payment_inst.booking_id,
                "payment_date" : payment_inst.payment_date,
                "payment_status" : payment_inst.payment_status,
                "amount" : payment_inst.amount,
                "email" : payment_inst.email,
                "notes" : payment_inst.notes
            })
            return 200, {"success": True}
        else:
            return "Booking not found"
    except pymongo.errors.DuplicateKeyError:
        return 400, {"error" : "Payment already exists"}
    
    except Exception as E:
        return 400, {"error" : str(E)}

def add_review(review_inst : Review):
    try:
        booking = db["bookings"].find_one({"_id" : review_inst.booking_id})

        if booking:
            status = db["reviews"].insert_one({
                "_id" : review_inst.id,
                "rating" : review_inst.rating,
                "booking_id" : review_inst.booking_id,
                "comment" : review_inst.comment,
                "created_at": datetime.datetime.utcnow(),
                "updated_at": datetime.datetime.utcnow()      
            })
            return 200, {"success": True}
        else:
            return "Booking not found"

    except pymongo.errors.DuplicateKeyError:
        return 400, {"error" : "Review already exists"}
    
    except Exception as E:
        return 400, {"error" : str(E)}

def get_all_users():
    try:
        users = [i for i in db.users.find()]
        # print(users)
        return users
        
    except Exception as E:
        return 400, {"error" : str(E)}  
    
def get_user_by_id(id):
    try:
        user = db.users.find_one({"_id" : id})
        return user
        
    except Exception as E:
        return 400, {"error" : str(E)}
    
def get_all_staffs():
    try:
        staffs = [i for i in db.staff.find()]
        return staffs
        
    except Exception as E:
        return 400, {"error" : str(E)}
    
def get_staff_by_id(id):
    try:
        staff = db.staff.find_one({"_id" : id})
        return staff
        
    except Exception as E:
        return 400, {"error" : str(E)}

def get_all_admins():
    try:
        admins = [i for i in db.admins.find()]
        return admins
        
    except Exception as E:
        return 400, {"error" : str(E)}

def get_admin_by_id(id):
    try:
        admin = db.admins.find_one({"_id" : id})
        return admin
        
    except Exception as E:
        return 400, {"error" : str(E)}

def get_all_customers():
    try:
        customers = [i for i in db.customers.find()]
        return customers
        
    except Exception as E:
        return 400, {"error" : str(E)}

def get_customer_by_id(id):
    try:
        customer = db.customers.find_one({"_id" : id})
        return customer
        
    except Exception as E:
        return 400, {"error" : str(E)}

def get_all_hotels():
    try:
        hotels = [i for i in db.hotels.find()]
        return hotels
        
    except Exception as E:
        return 400, {"error" : str(E)}

def get_hotel_by_id(id):
    try:
        hotel = db.hotels.find_one({"_id" : id})
        return hotel
        
    except Exception as E:
        return 400, {"error" : str(E)}

def get_all_rooms():
    try:
        rooms = [i for i in db.rooms.find()]
        return rooms
        
    except Exception as E:
        return 400, {"error" : str(E)}

def get_room_by_id(id):
    try:
        room = db.rooms.find_one({"_id" : id})
        return room
        
    except Exception as E:
        return 400, {"error" : str(E)}

def get_all_bookings():
    try:
        bookings = [i for i in db.bookings.find()]
        return bookings
        
    except Exception as E:
        return 400, {"error" : str(E)}

def get_booking_by_id(id):
    try:
        booking = db.bookings.find_one({"_id" : id})
        return booking
        
    except Exception as E:
        return 400, {"error" : str(E)}

def get_all_payments():
    try:
        payments = [i for i in db.payments.find()]
        return payments
        
    except Exception as E:
        return 400, {"error" : str(E)}

def get_payment_by_id(id):
    try:
        payment = db.payments.find_one({"_id" : id})
        return payment
        
    except Exception as E:
        return 400, {"error" : str(E)}

def get_all_reviews():
    try:
        reviews = [i for i in db.reviews.find()]
        return reviews
        
    except Exception as E:
        return 400, {"error" : str(E)}

def get_review_by_id(id):
    try:
        review = db.reviews.find_one({"_id" : id})
        return review
        
    except Exception as E:
        return 400, {"error" : str(E)}

def delete_user(id):
    try:
        total_count = 0
        for i in ["users", "admins", "customers", "staff", "bookings"]:
            status = db[i].delete_one({"_id": id})
            total_count += status.deleted_count
        return 200, {"status" : "Deleted {} record".format(total_count)}
    except Exception as E:
        return 400, {"error" : str(E)}

def delete_staff(id):
    try:
        status = db.staff.delete_one({"_id": id})
        return 200, {"status" : "Deleted {} record".format(status.deleted_count)}
    except Exception as E:
        return 400, {"error" : str(E)}

def delete_admin(id):
    try:
        status = db.admins.delete_one({"_id": id})
        return 200, {"status" : "Deleted {} record".format(status.deleted_count)}
    except Exception as E:
        return 400, {"error" : str(E)}

def delete_customer(id):
    try:
        status = db.customers.delete_one({"_id": id})
        return 200, {"status" : "Deleted {} record".format(status.deleted_count)}
    except Exception as E:
        return 400, {"error" : str(E)}

def delete_hotel(id):
    try:
        status = db.hotels.delete_one({"_id": id})
        status_room = db.rooms.delete_one({"hotel_id" : id})
        return 200, {"status" : "Deleted {} record".format(status.deleted_count + status_room.deleted_count)}
    except Exception as E:
        return 400, {"error" : str(E)}


def delete_room(id):
    try:
        status = db.rooms.delete_one({"_id": id})
        return 200, {"status" : "Deleted {} record".format(status.deleted_count)}
    except Exception as E:
        return 400, {"error" : str(E)}


def delete_booking(id):
    try:
        status = db.bookings.delete_one({"_id": id})
        return 200, {"status" : "Deleted {} record".format(status.deleted_count)}
    except Exception as E:
        return 400, {"error" : str(E)}


def delete_review(id):
    try:
        status = db.reviews.delete_one({"_id": id})
        return 200, {"status" : "Deleted {} record".format(status.deleted_count)}
    except Exception as E:
        return 400, {"error" : str(E)}

def update_user(id, data):
    data = json.loads(data.json())
    del data["id"]

    try:
        status = db.users.update_one({"_id": id}, {"$set": data}, upsert = True)
        if status.upserted_id:
            return 201, {"status" : "Inserted {} record".format(1)}
        return 200, {"status" : "Updated {} record".format(status.modified_count)}
    except Exception as E:
        return 400, {"error" : str(E)}

def update_staff(id, data):
    data = json.loads(data.json())
    data["updated_at"] = datetime.datetime.utcnow()
    del data["id"]

    try:
        status = db.staff.update_one({"_id": id}, {"$set": data}, upsert = True)
        if status.upserted_id:
            return 201, {"status" : "Inserted {} record".format(1)}
        return 200, {"status" : "Updated {} record".format(status.modified_count)}
    except Exception as E:
        return 400, {"error" : str(E)}

def update_admin(id, data):
    data = json.loads(data.json())

    data["updated_at"] = datetime.datetime.utcnow()
    del data["id"]

    try:
        status = db.admins.update_one({"_id": id}, {"$set": data}, upsert = True)
        if status.upserted_id:
            return 201, {"status" : "Inserted {} record".format(1)}
        return 200, {"status" : "Updated {} record".format(status.modified_count)}
    except Exception as E:
        return 400, {"error" : str(E)}

def update_customer(id, data):
    data = json.loads(data.json())
    data["updated_at"] = datetime.datetime.utcnow()
    del data["id"]

    try:
        status = db.customers.update_one({"_id": id}, {"$set": data}, upsert = True)
        if status.upserted_id:
            return 201, {"status" : "Inserted {} record".format(1)}
        return 200, {"status" : "Updated {} record".format(status.modified_count)}
    except Exception as E:
        return 400, {"error" : str(E)}

def update_hotel(id, data):
    data = json.loads(data.json())
    del data["id"]

    try:
        status = db.hotels.update_one({"_id": id}, {"$set": data}, upsert = True)
        if status.upserted_id:
            return 201, {"status" : "Inserted {} record".format(1)}
        return 200, {"status" : "Updated {} record".format(status.modified_count)}
    except Exception as E:
        return 400, {"error" : str(E)}

def update_room(id, data):
    data = json.loads(data.json())

    data["updated_at"] = datetime.datetime.utcnow()
    del data["id"]

    try:
        status = db.rooms.update_one({"_id": id}, {"$set": data}, upsert = True)
        if status.upserted_id:
            return 201, {"status" : "Inserted {} record".format(1)}
        return 200, {"status" : "Updated {} record".format(status.modified_count)}
    except Exception as E:
        return 400, {"error" : str(E)}

def update_booking(id, data):
    data = json.loads(data.json())
    del data["id"]

    try:
        status = db.bookings.update_one({"_id": id}, {"$set": data}, upsert = True)
        if status.upserted_id:
            return 201, {"status" : "Inserted {} record".format(1)}
        return 200, {"status" : "Updated {} record".format(status.modified_count)}
    except Exception as E:
        return 400, {"error" : str(E)}

def update_review(id, data):
    data = json.loads(data.json())

    data["updated_at"] = datetime.datetime.utcnow()
    del data["id"]

    try:
        status = db.reviews.update_one({"_id": id}, {"$set": data}, upsert = True)
        if status.upserted_id:
            return 201, {"status" : "Inserted {} record".format(1)}
        return 200, {"status" : "Updated {} record".format(status.modified_count)}
    except Exception as E:
        return 400, {"error" : str(E)}

def update_payment(id, data):
    data = json.loads(data.json())
    del data["id"]

    try:
        status = db.payments.update_one({"_id": id}, {"$set": data}, upsert = True)
        if status.upserted_id:
            return 201, {"status" : "Inserted {} record".format(1)}
        return 200, {"status" : "Updated {} record".format(status.modified_count)}
    except Exception as E:
        return 400, {"error" : str(E)}