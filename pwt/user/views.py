from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User,OTP
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

#  -------------------------------------------------------- user_create_view -----------------------------------------------------------------

@api_view(['POST'])
def user_create_view(request):
    serializer = UserSerializer(data=request.data)
    
    try:
        if User.objects.filter(email=request.data.get('email')).exists():
            return Response(
                {"error": "A user with this email already exists."}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        if User.objects.filter(username=request.data.get('username')).exists():
            return Response(
                {"error": "A user with this username already exists."}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except ValidationError as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



#  -------------------------------------------------------- user_list_view_all -----------------------------------------------------------------

@api_view(['GET'])
def user_list_view_all(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


#  -------------------------------------------------------- user_detail_view -----------------------------------------------------------------


@api_view(['GET'])
def user_detail_view(request):
    user_pk = request.headers.get('pk')
    if not user_pk:
        return Response(
            {"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
      
        user = User.objects.get(pk=user_pk)
    except User.DoesNotExist:
        return Response(
            {"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND
        )


    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)








#  -------------------------------------------------------- user_update_view -----------------------------------------------------------------



@api_view(['PUT'])
def user_update_view(request):
   
    user_pk = request.headers.get('pk')
    if not user_pk:
        return Response(
            {"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
     
        user = User.objects.get(pk=user_pk)
    except User.DoesNotExist:
        return Response(
            {"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

  
    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        user = serializer.save()
      
        if 'password' in request.data:
            user.password = make_password(request.data['password'])
            user.save()
        return Response(
            {"message": "User updated successfully", "data": serializer.data},
            status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





#  -------------------------------------------------------- user_update_patch_view -----------------------------------------------------------------


@api_view(['PATCH'])
def user_update_patch_view(request):
  
    user_pk = request.headers.get('pk')
    if not user_pk:
        return Response(
            {"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        
        user = User.objects.get(pk=user_pk)
    except User.DoesNotExist:
        return Response(
            {"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

  
    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        user = serializer.save()
        
        if 'password' in request.data:
            user.password = make_password(request.data['password'])
            user.save()
        return Response(
            {"message": "User updated successfully", "data": serializer.data},
            status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#  -------------------------------------------------------- user_delete_view -----------------------------------------------------------------


@api_view(['DELETE'])
def user_delete_view(request):
   
    user_pk = request.headers.get('pk')
    if not user_pk:
        return Response(
            {"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
      
        user = User.objects.get(pk=user_pk)
    except User.DoesNotExist:
        return Response(
            {"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    # Delete the user
    user.delete()
    return Response(
        {"message": "User deleted successfully"},
        status=status.HTTP_204_NO_CONTENT
    )



# ******************************************************** OTP SYSTEM****************************************************************

# ------------------------------------------------------------OTP SYSTEM -------------------------------------------------------------

# import random
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import User, OTP
# from .serializers import OTPRequestSerializer, OTPVerifySerializer
# from django.utils import timezone
# from datetime import timedelta

# def create_otp_code(length=6):
#     """Generate a random OTP of the given length."""
#     return ''.join([str(random.randint(0, 9)) for _ in range(length)])

# # ---------------------------------------------------------------------GENERATE OTP ---------------------------------------------------------



# @api_view(["POST"])  # Ensure the function is set up to accept POST requests
# def generate_otp(request):
#     serializer = OTPRequestSerializer(data=request.data)
#     if serializer.is_valid():
#         email = serializer.validated_data['email']
#         user = User.objects.filter(email=email).first()
#         if user is None:
#             return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

#         otp_code = create_otp_code()
#         expiration_time = timezone.now() + timedelta(minutes=5)

#         # Remove any existing OTP for this email
#         OTP.objects.filter(email=email).delete()

#         # Create and save new OTP
#         OTP.objects.create(user=user, otp=otp_code, email=email, expiry_time=expiration_time)

#         # Send OTP via email
#         send_otp_email(email, otp_code)

#         return Response({"message": "OTP generated and sent successfully to the provided email address."})

#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # -------------------------------------------------------------VERIFY OTP -----------------------------------------------------------------

# @api_view(["POST"])
# def verify_otp(request):
#     serializer = OTPVerifySerializer(data=request.data)
#     if serializer.is_valid():
#         email = serializer.validated_data['email']
#         otp_code = serializer.validated_data['otp_code']

#         try:
#             otp_entry = OTP.objects.get(email=email, otp=otp_code)

#             if otp_entry.is_valid():
#                 otp_entry.user.is_verified = True
#                 otp_entry.user.save()

#                 otp_entry.delete()
#                 return Response({"message": "OTP verified successfully."})
#             else:
#                 return Response({"error": "OTP has expired."}, status=status.HTTP_400_BAD_REQUEST)

#         except OTP.DoesNotExist:
#             return Response({"error": "Invalid OTP."}, status=status.HTTP_400_BAD_REQUEST)

#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# =======================================================================================================================================

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

# ------------------------------------------------------------------logging_user--------------------------------------------------------------

@api_view(["POST"])
def logging_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    # Fetch the user based on the provided email
    db_user = User.objects.filter(email=email).first()

    if not db_user:
        raise NotFound("User with this email does not exist")

    # Check if the user is active
    if not db_user.is_active:
        raise ValidationError("User account is not active")

    # Check if the user is not deleted
    if db_user.is_deleted:
        raise ValidationError("User account has been deleted")

    # Check if the user is verified
    if not db_user.is_verified:
        raise ValidationError("User account is not verified")

    # Check if the provided password is correct
    if not check_password(password, db_user.password):
        raise ValidationError("Password is incorrect")

    # Generate JWT tokens
    refresh = RefreshToken.for_user(db_user)
    access_token = str(refresh.access_token)

    return Response({
        "access_token": access_token,
        "refresh_token": str(refresh)
    })






# ----------------------------------------------------------reset password -----------------------------------------------------
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
# Import other necessary modules

def generate_test_token(user_id):
    payload = {
        'user_id': str(user_id),  # Ensure user_id is stringified if using UUID
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token

@api_view(["PUT"])
def reset_password(request):
    new_password = request.data.get('new_password')
    token = request.data.get('token')

    if not new_password or not token:
        return Response({"error": "Both new_password and token are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Decode the JWT token to get user information
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user_id = payload.get('user_id')

        if not user_id:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch user from the database
        user = User.objects.filter(id=user_id, is_active=True).first()

        if not user:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # Update the user's password
        user.password = make_password(new_password)
        user.save()

        return Response({"message": "Password reset successfully"}, status=status.HTTP_200_OK)

    except jwt.ExpiredSignatureError:
        return Response({"error": "Token has expired"}, status=status.HTTP_400_BAD_REQUEST)
    except jwt.InvalidTokenError:
        return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# =========================================================================================================================================






# from rest_framework.exceptions import NotFound, ValidationError
# from django.utils import timezone
# from datetime import timedelta
# from .models import User, OTP
# from pwt.settings import generate_otp, get_token, decode_token_user_id, decode_token_user_email,decode_token_password
# from django.contrib.auth.hashers import make_password, check_password
# @api_view(["POST"])
# def logging_user(request):
#     email = request.data.get('email')
#     password = request.data.get('password')
#     db_user = User.objects.filter(
#         email=email, is_active=True, is_deleted=False, is_verified=True
#     ).first()

#     if not db_user:
#         raise NotFound("customer is not found")

#     if not check_password(password, db_user.password):
#         raise ValidationError("Password is incorrect")

#     # Generate the access token
#     access_token = get_token(str(db_user.id), email, password)
#     return Response({"access_token": str(access_token)})



# @api_view(["PUT"])
# def reset_password(request):
#     newpass = request.data.get('newpass')
#     token = request.data.get('token')
#     id = decode_token_user_id(token)
#     email = decode_token_user_email(token)
#     password = decode_token_password(token)

#     db_user = User.objects.filter(id=id, email=email, is_active=True).first()
#     if not db_user:
#         raise NotFound("Customer data is not found")

#     if check_password(password, db_user.password):
#         db_user.password = make_password(newpass)
#         db_user.save()
#         return Response({"message": "Password reset successfully"})
#     else:
#         raise ValidationError("Old password does not match")



# @api_view(["PUT"])
# def reregister_user(request):
#     email = request.data.get('email')
#     password = request.data.get('password')
#     token = request.headers.get('Authorization')
    
#     if not token:
#         raise ValidationError("Token is missing from headers")
    
#     id = decode_token_user_id(token)

#     db_user = User.objects.filter(id=id).first()
#     if not db_user:
#         raise NotFound("Customer not found")

#     if not db_user.is_active and db_user.is_deleted:
#         if check_password(password, db_user.password):
#             db_user.is_active = True
#             db_user.is_deleted = False
#             db_user.save()
#             return Response({"message": "Successfully re-registered"})
#     else:
#         raise ValidationError("Email or password does not match")



# @api_view(["PUT"])
# def forget_password(request):
#     user_newpass = request.data.get('user_newpass')
#     token = request.data.get('token')
#     user_id = decode_token_user_id(token)

#     db_user = User.objects.filter(
#         id=user_id, is_active=True, is_verified=True, is_deleted=False
#     ).first()

#     if not db_user:
#         raise NotFound("customer not found")

#     if not db_user.is_verified:
#         raise ValidationError("customer is not verified")

#     db_user.password = make_password(user_newpass)
#     db_user.save()
#     return Response({"message": "Password reset successfully"})





# ---------------------------------------------------------send_otp_email---------------------------------------------------

import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, OTP
from .serializers import OTPRequestSerializer
from django.utils import timezone
from datetime import timedelta
from django.views.decorators.csrf import csrf_exempt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
from django.core.exceptions import ValidationError

logger = logging.getLogger(__name__)

# Function to send OTP via email
def send_otp_email(email: str, otp_code: str):
    logger.info(f"Sending OTP email to: {email}")
    sender_email = "ujasmungla@gmail.com"
    password = "wfrdhevqfopcssre"
    subject = "Your OTP Code"
    message_text = f"Your OTP is {otp_code}, valid for 5 minutes."

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = email
    message["Subject"] = subject
    message.attach(MIMEText(message_text, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, email, message.as_string())
        server.close()
        logger.info(f"OTP email sent successfully to: {email}")
    except smtplib.SMTPException as e:
        logger.error(f"Failed to send OTP email to {email}: {str(e)}")
        raise ValidationError("Failed to send email due to an SMTP error.")
    except Exception as e:
        logger.error(f"An unexpected error occurred while sending OTP email to {email}: {str(e)}")
        raise ValidationError("Failed to send email due to an unexpected error.")

# Function to create a random OTP code
def create_otp_code(length=6):
    return ''.join([str(random.randint(0, 9)) for _ in range(length)])

# View for generating OTP
@csrf_exempt  # Exempts the view from CSRF protection
@api_view(["POST"])
def generate_otp(request):
    serializer = OTPRequestSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        user = User.objects.filter(email=email).first()
        if user is None:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        otp_code = create_otp_code()
        expiration_time = timezone.now() + timedelta(minutes=5)

        # Delete any existing OTPs for this user
        OTP.objects.filter(email=email).delete()

        # Save new OTP to the database
        OTP.objects.create(user=user, otp=otp_code, email=email, expiry_time=expiration_time)

        # Send OTP email
        try:
            send_otp_email(email, otp_code)
            return Response({"message": "OTP generated and sent successfully to the provided email address."})
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# ------------------------------------------------------------------VERIFY OTP ---------------------------------------------------------------

from .serializers import OTPVerifySerializer


@api_view(["POST"])
def verify_otp(request):
    serializer = OTPVerifySerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        otp_code = serializer.validated_data['otp']

        # Fetch the OTP entry from the database
        otp_entry = OTP.objects.filter(email=email, otp=otp_code).first()

        if otp_entry is None:
            return Response({"error": "Invalid OTP or email."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the OTP has expired
        if timezone.now() > otp_entry.expiry_time:
            return Response({"error": "OTP has expired."}, status=status.HTTP_400_BAD_REQUEST)

        # OTP is valid; proceed with further actions
        user = otp_entry.user

        # Optionally, delete the OTP after successful verification
        otp_entry.delete()

        # Update the user's `is_verified` status if not already verified
        if not user.is_verified:
            user.is_verified = True
            user.save()

        return Response({"message": "OTP verified successfully.", "user_id": user.id})

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)