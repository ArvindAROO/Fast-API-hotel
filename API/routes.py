from API import app

from schema import *
from model import *


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/users/")
def insert_users(user: User):
    # get users from the body
    status = add_user(user)
    return status

@app.post("/staff/")
def insert_staff(staff :Staff):
    status = add_staff(staff)
    return status

@app.post("/admin/")
def insert_admin(admin :Admin):
    status = add_admin(admin)
    return status

@app.post("/customer/")
def insert_customer(cust :Customer):
    status = add_customer(cust)
    return status

@app.post("/hotel/")
def insert_hotel(hotel :Hotel):
    status = add_hotel(hotel)
    return status

@app.post("/room/")
def insert_room(room :Room):
    status = add_room(room)
    return status

@app.post("/booking/")
def insert_booking(booking :Booking):
    status = add_booking(booking)
    return status

@app.post("/review/")
def insert_review(review :Review):
    status = add_review(review)
    return status

@app.post("/payment/")
def insert_payment(payment :Payment):
    status = add_payment(payment)
    return status

@app.get("/users/")
def get_users():
    users = get_all_users()
    return users

@app.get("/users/{user_id}")
def get_user(user_id : str):
    user = get_user_by_id(user_id)
    return user

@app.get("/staff/")
def get_staff():
    staff = get_all_staffs()
    return staff

@app.get("/staff/{staff_id}")
def get_staff(staff_id : str):
    staff = get_staff_by_id(staff_id)
    return staff

@app.get("/admin/")
def get_admin():
    admin = get_all_admins()
    return admin

@app.get("/admin/{admin_id}")
def get_admin(admin_id : str):
    admin = get_admin_by_id(admin_id)
    return admin


@app.get("/customer/")
def get_customer():
    customer = get_all_customers()
    return customer

@app.get("/customer/{cust_id}")
def get_customer(cust_id : str):
    customer = get_customer_by_id(cust_id)
    return customer

@app.get("/hotel/")
def get_hotel():
    hotel = get_all_hotels()
    return hotel

@app.get("/hotel/{hotel_id}")
def get_hotel(hotel_id : str):
    hotel = get_hotel_by_id(hotel_id)
    return hotel

@app.get("/room/")
def get_room():
    room = get_all_rooms()
    return room

@app.get("/room/{room_id}")
def get_room(room_id : str):
    room = get_room_by_id(room_id)
    return room

@app.get("/booking/")
def get_booking():
    booking = get_all_bookings()
    return booking

@app.get("/booking/{booking_id}")
def get_booking(booking_id : str):
    booking = get_booking_by_id(booking_id)
    return booking

@app.get("/review/")
def get_review():
    review = get_all_reviews()
    return review

@app.get("/review/{review_id}")
def get_review(review_id : str):
    review = get_review_by_id(review_id)
    return review

@app.get("/payment/")
def get_payment():
    payment = get_all_payments()
    return payment

@app.get("/payment/{payment_id}")
def get_payment(payment_id : str):
    payment = get_payment_by_id(payment_id)
    return payment

@app.delete("/users/{user_id}")
def user_delete(user_id : str):
    status = delete_user(user_id)
    return status


@app.delete("/staff/{staff_id}")
def staff_delete(staff_id : str):
    status = delete_staff(staff_id)
    return status

@app.delete("/admin/{admin_id}")
def admin_delete(admin_id : str):
    status = delete_admin(admin_id)
    return status

@app.delete("/customer/{cust_id}")
def customer_delete(cust_id : str):
    status = delete_customer(cust_id)
    return status

@app.delete("/hotel/{hotel_id}")
def hotel_delete(hotel_id : str):
    status = delete_hotel(hotel_id)
    return status

@app.delete("/room/{room_id}")
def room_delete(room_id : str):
    status = delete_room(room_id)
    return status

@app.delete("/booking/{booking_id}")
def booking_delete(booking_id : str):
    status = delete_booking(booking_id)
    return status

@app.delete("/review/{review_id}")
def review_delete(review_id : str):
    status = delete_review(review_id)
    return status

@app.put("/users/{user_id}")
def user_update(user_id : str, user : User):
    status = update_user(user_id, user)
    return status

@app.put("/staff/{staff_id}")
def staff_update(staff_id : str, staff : Staff):
    status = update_staff(staff_id, staff)
    return status

@app.put("/admin/{admin_id}")
def admin_update(admin_id : str, admin : Admin):
    status = update_admin(admin_id, admin)
    return status

@app.put("/customer/{cust_id}")
def customer_update(cust_id : str, cust : Customer):
    status = update_customer(cust_id, cust)
    return status

@app.put("/hotel/{hotel_id}")
def hotel_update(hotel_id : str, hotel : Hotel):
    status = update_hotel(hotel_id, hotel)
    return status

@app.put("/room/{room_id}")
def room_update(room_id : str, room : Room):
    status = update_room(room_id, room)
    return status

@app.put("/booking/{booking_id}")
def booking_update(booking_id : str, booking : Booking):
    status = update_booking(booking_id, booking)
    return status

@app.put("/review/{review_id}")
def review_update(review_id : str, review : Review):
    status = update_review(review_id, review)
    return status

@app.put("/payment/{payment_id}")
def payment_update(payment_id : str, payment : Payment):
    status = update_payment(payment_id, payment)
    return status
