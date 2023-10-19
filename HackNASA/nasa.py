import os
from pynput import keyboard
import time
import random

class Nasa:

    def __init__(self):
        self.points = 0
        self.rocket_pic = "rocket.txt"
        self.user_move = ""
        self.tries = 0
        self.seconds = 0

        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()
        os.system("clear")

        os.system("echo Hack NASA | figlet")
        print("Confuse the rocket's control system to blow it up before it reaches the moon!")

        while True:
            self.pilot = input("Choose the pilot of the rocket:\n1) Sail Aviator\n2) Captain who's on to every dodge\n3) Stunt Pilot\n")
            if self.pilot in ["1", "2", "3"]:
                break
        
        match self.pilot:
            case "1":
                self.seconds = 1
            case "2":
                self.seconds = 0.75
            case "3":
                self.seconds = 0.5		

        os.system("clear")
        while self.points < 10:
            for i in range(20 - self.tries):
               print("\n")
            os.system("cat {}".format(self.rocket_pic))
            start_time = time.time()
            correct_move = random.choice(["y", "m", "x", "n"])
            print("Press: " + correct_move)
            while time.time() < start_time + self.seconds:
               pass
            self.tries += 1
            os.system("clear")
            if self.user_move == correct_move:
                self.points += 1
            if self.points > 4:
                self.rocket_pic = "rocket_some_fire.txt"
            if self.points > 7:
                self.rocket_pic = "rocket_full_fire.txt"
            if self.points == 10:
                print("🔥           🔥")
                time.sleep(0.1)
                print("    🔥   🔥🔥")
                time.sleep(0.1)
                print("  🔥  🔥🔥")
                time.sleep(0.1)
                print("   🔥 🔥  🔥")
                time.sleep(0.1)
                print("  🔥  🔥🔥")
                time.sleep(0.1)
                print("    🔥🔥  🔥 🔥")
                time.sleep(0.1)
                print(" 🔥     🔥")
                print("The Rocket is Dead!🔥 You Win!")
                break
            if self.tries == 20:
                print("The Rocket reached the Moon 🌑 You loose")
                break

    def on_press(self, key):
        try:
            self.user_move = key.char
        except:
            pass

Nasa()


