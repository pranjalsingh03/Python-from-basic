import speech_recognition as sr
r = sr.Recognizer()
my_mic = sr.Microphone() 
with my_mic as source:
    print("Say now!!!!")
    r.adjust_for_ambient_noise(source) 
    audio = r.listen(source) 
print(r.recognize_google(audio)) 