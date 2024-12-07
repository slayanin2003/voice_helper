import speech_recognition as sr
import pyttsx3
from pyttsx3 import voice


def speak_text(text: str) -> None:
    print("Воспроизведение...")
    engine = pyttsx3.init()
    engine.setProperty('voice', 'ru')
    engine.setProperty('rate', 150)  # Скорость речи
    engine.setProperty('volume', 1)  # Громкость (от 0.0 до 1.0)
    engine.say(text)
    engine.runAndWait()


def main() -> None:
    r = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                print("Говорите...")
                audio = r.listen(source)
                print("Голос записан!")
                text = r.recognize_google(audio, language='ru')
                text = text.lower()
                speak_text(text)
                break
        except sr.RequestError:
            print("Ошибка какая-то")


if __name__ == '__main__':
    main()
