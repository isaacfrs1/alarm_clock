from playsound import playsound
import time

CLEAR_AND_RETURN = "\033[H"
def alarm(seconds):
    time_elapsed = 0

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}{minutes_left:02d}: {seconds_left:02d}")
    playsound('alarm.mp3')

minutes = int(input("Diga os minutos do alarme: "))
seconds = int(input("Diga os segundos do alarme: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)