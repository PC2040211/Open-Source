from django.conf import settings 
from django.core.mail import send_mail 








def send_account_activation_email(email,email_token):
    subject='Yours accpoiunts needs to be verified'
    email_from=settings.EMAIL_HOST_USER 
    message=f'hi,click on this link     to activivateed your account{email_token}'
    send_mail(subject,message,email_from,[email])