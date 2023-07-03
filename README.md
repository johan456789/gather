# Gather

## Setup

### Install prerequisites

```
pip install -r requirements.txt
```

### Set up environment variables in .env

Create a .env file in the root directory of the project and add the following variables:

```
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret_key
SQLALCHEMY_TRACK_MODIFICATIONS=False
TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_auth_token
```
