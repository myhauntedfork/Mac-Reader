import subprocess
import platform

message = input("What would you like you MAC to say?\n>> ")
def say_something(txt):
        system = platform.system()
        try:
                if system == "Darwin":
                        subprocess.run(["say", txt])
        except Exception as e:
                print(f"Error: {e}")
say_something(message)
