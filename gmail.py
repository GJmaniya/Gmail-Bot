# Import necessary libraries for email functionality and speech recognition
import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

# Initialize the speech recognition and text-to-speech engines
listener = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def talk(text):
    engine.say(text)
    engine.runAndWait()


# Function to get user input through speech
def get_info():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        talk("plase talk again")

# Function to send an email
def send_email(receiver, subject, body):
    # Set up the SMTP server and login credentials
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("your email id", "password")

    # Create an EmailMessage object and set its properties
    email=  EmailMessage()
    email['From'] = 'your email id'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(body)

    # Send the email
    server.send_message(email)

# Dictionary mapping names to email addresses
email_list = {
    'name':'email id'
}

# Function to get email information from the user and send the email
def get_email_info():
    talk("to whom you want to send email")
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk("what is the subject of your mail?")
    subject = get_info()
    talk("tell me the text in your email")
    body = get_info()
    send_email(receiver, subject, body)

# Call the function to get email information and send the email
get_email_info()
talk("send a mail a success fully!")
print("Thank you")