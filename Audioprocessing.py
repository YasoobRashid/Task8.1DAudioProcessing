import RPi.GPIO as GPIO
import speech_recognition as sr
import time

# GPIO setup
GPIO.setmode(GPIO.BOARD)
led_pin = 12
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setwarnings(False)  # Suppress GPIO warnings

# Initialize speech recognition
recognizer = sr.Recognizer()

while True:
    # Capture audio from the microphone
    with sr.Microphone() as mic:
        print("Please say a command...")
        audio_input = recognizer.listen(mic)

    try:
        # Convert the audio to text using Google Speech Recognition
        speech_text = recognizer.recognize_google(audio_input)
        print(f"Recognized speech: {speech_text}")

        # Check if the command is to turn the LED on or off
        if "on" in speech_text.lower():
            print("Turning LED on")
            GPIO.output(led_pin, GPIO.HIGH)
        elif "off" in speech_text.lower():
            print("Turning LED off")
            GPIO.output(led_pin, GPIO.LOW)

    except sr.UnknownValueError:
        # If the speech is not understood
        print("Sorry, I couldn't understand the command")
    except sr.RequestError as error:
        # Handle any request issues
        print(f"Could not request results; {error}")

    # Pause for a second before listening again
    time.sleep(1)
