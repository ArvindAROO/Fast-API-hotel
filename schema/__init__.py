from pydantic import BaseModel, ValidationError, validator


class User(BaseModel):
    id: str 
    user_name: str
    email : str
    email_verified : bool = False
    password_hash : str

    @validator('id')
    def id_len_check(cls, v):
        if len(v) < 5:
            raise ValidationError('ID must be longer than 5 characters')
        return v.title()
    


class Hotel(BaseModel):
    id : str
    name : str
    location : str 
    state : str
    rating : float = 0.0
    image_link : str
    gym_available : bool = False
    food_available : bool = False
    allows_booking : bool = False

    @validator('id')
    def hotel_id_len_check(cls, v):
        if len(v) < 5:
            raise ValueError('ID must be longer than 5 characters')
        return v.title()

    @validator('rating')
    def hotel_rating_must_be_between_0_and_5(cls, v):
        if v < 0 or v > 5:
            raise ValueError('Rating must be between 0 and 5')
        return v.title()
    
    

class Admin(BaseModel):
    id : str
    name : str
    mobile : str
    mobile_verified : bool = False
    dob : str 
    active : bool = False

    
class Staff(BaseModel):
    id : str
    name : str
    mobile : str
    mobile_verified : bool = False
    hotel_id : str 
    rating : float = 0.0
    

    @validator('rating')
    def staff_rating_must_be_between_0_and_5(cls, v):
        if v < 0 or v > 5:
            raise ValueError('Rating must be between 0 and 5')
        return v

class Customer(BaseModel):
    id : str
    name : str
    mobile : str
    mobile_verified : bool = False
    dob : str
    active : bool = False


class Room(BaseModel):
    id : str
    hotel_id : str
    room_type : str
    room_number : int 
    price : float
    rating : float = 0.0
    image_link : str = ""

    @validator('id')
    def room_id_check(cls, v):
        if len(v) < 5:
            raise ValueError('ID must be longer than 5 characters')
        return v.title()

    @validator('rating')
    def room_rating_must_be_between_0_and_5(cls, v):
        if v < 0 or v > 5:
            raise ValueError('Rating must be between 0 and 5')
        return v

class Booking(BaseModel):
    id : str
    room_id : str
    customer_id : str
    check_in : str 
    check_out : str
    total_price : float = 0.0
    booking_status : str

    @validator('id')
    def booking_id_len_check(cls, v):
        if len(v) < 5:
            raise ValueError('ID must be longer than 5 characters')
        return v.title()


class Payment(BaseModel):
    id : str
    booking_id : str
    payment_date : str
    payment_status : str
    total_price : float = 0.0
    amount : float = 0.0
    email : str
    notes : str = ""

    @validator('id')
    def payment_id_len_check(cls, v):
        if len(v) < 5:
            raise ValueError('ID must be longer than 5 characters')
        return v.title()


class Review(BaseModel):
    id : str
    booking_id : str
    comment : str = ""
    rating : float = 0.0

    @validator('id')
    def review_id_len_check(cls, v):
        if len(v) < 5:
            raise ValueError('ID must be longer than 5 characters')
        return v.title()

    @validator('rating')
    def review_rating_must_be_between_0_and_5(cls, v):
        if v < 0 or v > 5:
            raise ValueError('Rating must be between 0 and 5')
        return v