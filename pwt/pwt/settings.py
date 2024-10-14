from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2tod@-we&(x84e%sza226(=7e$!d9*+a*u7-1j%s&8w_j+_u$('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'user',
    'workout',
    'exercise',
    'exercise_library',
    'progress',
    'goal',
    'meal_plane',
    'meal',
    'meal_ingredients',
    
    'rest_framework_simplejwt',  # Ensure this is the name of your app
]







MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # Ensure this is present
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'pwt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pwt.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ujasmungla@gmail.com'
EMAIL_HOST_PASSWORD = 'wfrdhevqfopcssre'
DEFAULT_FROM_EMAIL = 'ujasmungla@gmail.com'



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    # Other settings...
}
from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': 'your_secret_key_here',
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

}



from django.core.mail import EmailMessage
from django.conf import settings
import random

def generate_otp():
    """Generate a 6-digit OTP"""
    return str(random.randint(100000, 999999))

def send_otp_email(receiver_email, otp):
    """Send an OTP email to the specified receiver email"""
    subject = "Your OTP Code"
    message_text = f"Your OTP is {otp} which is valid for 1 minute"

    # Create the email message
    email = EmailMessage(
        subject=subject,
        body=message_text,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[receiver_email]
    )

    try:
        email.send()
        print("Mail sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")



        AUTH_USER_MODEL = 'user.CustomUser'



from datetime import datetime, timedelta
import jwt
from django.conf import settings
from django.core.exceptions import ValidationError

def get_token(user_id, email, expiration_minutes=30):
    """Generate a JWT token for the user."""
    payload = {
        'user_id': user_id,
        'email': email,
        'exp': datetime.utcnow() + timedelta(minutes=expiration_minutes)
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token

def decode_token_user_id(token):
    """Decode the JWT token to retrieve the user ID."""
    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return decoded_token['user_id']
    except jwt.ExpiredSignatureError:
        raise ValidationError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValidationError("Invalid token")
    
def decode_token_user_email(token):
    """Decode the JWT token to retrieve the user email."""
    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return decoded_token['email']
    except jwt.ExpiredSignatureError:
        raise ValidationError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValidationError("Invalid token")


def decode_token_password(token):
    """Decode the JWT token to retrieve the user password."""
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return decoded_token['password']
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")








CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False


from django.core.mail import send_mail

def create_otp_code(length=6):
    """Generate a random OTP of the given length."""
    return ''.join([str(random.randint(0, 9)) for _ in range(length)])


def send_otp_via_email(sender_email, receiver_email, email_password, otp_code):
    """Send an OTP via email."""
    try:
        subject = 'Your OTP Code'
        message = f'Your OTP code is {otp_code}. It is valid for 10 minutes.'
        send_mail(subject, message, sender_email, [receiver_email], fail_silently=False)
        return True, "Email sent successfully"
    except Exception as e:
        return False, str(e)
    
# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ujasmungla@gmail.com'
EMAIL_HOST_PASSWORD = 'wfrdhevqfopcssre'
DEFAULT_FROM_EMAIL = 'ujasmungla@gmail.com'
