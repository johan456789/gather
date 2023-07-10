import app    #need to figure out what the equivalent of create_app in our function is

#create an instance of the flask application with a fixture

#def test_client...#

def test_home_page():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'When can we gather again?' in response.data
    assert b'Register' in response.data
    assert b'Login' in response.data

def test_invalid_home_page():

    response = test_client.post('/')
    assert response.status_code == 405
    assert b'When can we gather again?' not in response.data
    #hceck that the header text is not in the response

def test_login_page():

    response = test_client.get('/login')
    assert response.status_code == 200
    assert b'Login' in response.data
    assert b'Email' in response.data
    assert b'Password' in response.data

def test_submit_login_page():

    response1 = test_client.post('/login')
    #same code as test_upload_page?

def test_submit_register_page():

    response1 = test_client.post('/register')
    #same code as test_upload_page?


def test_register_page():
    response = test_client.get('/register')
    assert response.status_code == 200
    assert b'Welcome to Gather' in response.data
    assert b'Full name' in response.data
    assert b'Email' in response.data
    assert b'Password' in response.data
    assert b'Contact' in response.data
    assert b'Create Account' in response.data #button


def test_upload_page():
    response = test_client.get('/upload') #ok to do this if no 'get'?
    assert response.status_code == 200
    assert b'Reunion' in response.data
    assert b'let\'s gather again' in response.data
    assert b'Friend Name' in response.data
    assert b'Message' in response.data
    assert b'Upload' in response.data
    assert b'Submit' in response.data #not sure if buttons are text

def test_invalid_upload_page():

    response = test_client.post('/upload')
    assert response.status_code == 405
    assert b'Reunion' not in response.data
