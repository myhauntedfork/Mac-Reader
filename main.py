import subprocess
import platform
import re

def say(txt):
    slang = {
        r"\bidk\b": "I don't know",
        r"\bidek\b": "I don't even know",
        r"\bidc\b": "I don't care",
        r"\bomg\b": "oh my god",
        r"\bthx\b": "thanks",
        r"\bwdym\b": "what do you mean",
        r"\bpls\b": "please",
        r"\bim\b": "I'm",
        r"\bimh\b": "I'm having a hard time",
        r"\bidli\b": "I don't like it",
        r"\bimo\b": "in my opinion",
        r"\bbrb\b": "be right back",
        r"\bbtw\b": "by the way",
        r"\bfyi\b": "for your information",
        r"\bbc\b": "because",
        r"\btbh\b": "to be honest",
        r"\bsry\b": "sorry",
        r"\bnvm\b": "never mind",
        r"\bsmh\b": "shaking my head",
        r"\bnp\b": "no problem",
        r"\byolo\b": "you only live once",
        r"\bafk\b": "away from keyboard",
        r"\btbf\b": "to be fair",
        r"\blmk\b": "let me know",
        r"\birl\b": "in real life",
        r"\bdm\b": "direct message",
        r"\bikr\b": "I know, right",
        r"\bbbl\b": "be back later",
        r"\bily\b": "I love you",
        r"\bgg\b": "good game",
        r"\bwtf\b": "what the heck",
        r"\bwth\b": "what the heck",
        r"\btfw\b": "that feeling when",
        r"\bfr\b": "for real",
        r"\bwya\b": "where you at",
        r"\bhmu\b": "hit me up",
        r"\btho\b": "though",
        r"\bwbu\b": "what about you",
        r"\blmao\b": "laughing my ass off",
        r"\bltr\b": "later",
        r"\bidgaf\b": "I don't give a darn",
        r"\bstfu\b": "shut up",
        r"\bsu\b": "shut up",
        r"\byt\b": "YouTube",
        r"\bgm\b": "good morning",
        r"\bgn\b": "good night",
        r"\bgtg\b": "got to go",
        r"\bg2g\b": "got to go",
    }

    for slang, replacement in slang.items():
        txt = re.sub(slang, replacement, txt, flags=re.IGNORECASE)

    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(["say", txt])
        else:
            print("Error: The software is compatible only with Darwin (macOS) systems.")
    except Exception as e:
        print(f"Error: {e}")

print("What would you like your MAC to say? (type 'exit' to quit)")
while True:
    message = input(">> ")
    if message.lower() == "exit":
        break
    say(message)
