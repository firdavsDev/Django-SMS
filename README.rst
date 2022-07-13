===============================
Django send SMS using API(uz)
===============================

Quick start
------------
1. Create a new project
2. Add the following to your settings.py file:

    INSTALLED_APPS = (
        ...
        'SMS',
    )

3. Add the following to your urls.py file:
    url(r'^sms/', include('SMS.urls')),
4. Run ``python manage.py migrate`` to create the database tables
5. Start your Django development server
6. Go to http://localhost:8000/sms/send_sms/
7. Enter your phone number and message and click Send
8. Check your terminal for a response and Django admin will tell you if it was successful or not
9. You could use call ``from SMS.sms_utils import SMS_Sender`` to get the SMS class and send sms using by the way ``SMS_Sender(phone_number, message).SendSmsOneContact()`` it returns a response
10. Don't forget to add ``SMS`` to your INSTALLED_APPS list and add 
SMS_SETTINGS = {
    "SMS_URL": "http://91.204.239.44/broker-api/send",
    "SMS_LOGIN": "LOGIN",
    "SMS_PASSWORD": "PASSWORD"
 
} 
set in your settings.py file
