import subprocess

message = input("What would you like you MAC to say?\n>> ")
def say_something(txt):
        subprocess.run(["say", txt])
say_something(message)
