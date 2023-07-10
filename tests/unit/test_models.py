from app.models import User, Photo
#not sure if this is the correct way to import

def test_new_user():
    """
    GIVEN a User Model
    WHEN a new User is created
    THEN check the name, email, password, contact fields are defined correctly
    """
    user = User('John',
                'johndoe@example.com',
                'password',
                '0987654321')
    assert user.name == 'John'
    assert user.email == 'johndoe@example.com'
    assert user.password == 'password'
    assert user.contact == '0987654321'

def test_new_photo():
       
    photo = Photo(friend_name='Mary',
                  friend_contact='1234567890',
                  photo_path='photo.jpg',
                  contact='0987654321',
                  uploader_id=1)
       
    assert photo.friend_name == 'Mary'
    assert photo.friend_contact == '1234567890'
    assert photo.photo_path == 'photo.jpg'
    assert photo.contact == '0987654321'
    assert photo.uploader_id == '1'