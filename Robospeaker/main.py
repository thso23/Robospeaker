import pyttsx3


if __name__ == '__main__':
    engine = pyttsx3.init()
    print("welcome to Robospeaker 1.1. created by sameer")
    while True:
        x = input("enter what you want  me to speak :")
        if x == "q":
            engine.say( "bye bye friends")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()
