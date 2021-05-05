import the_voice
import main_archit
import main_harshit

import random

greet_text = ["What are my orders?",
              "Fully functional!",
              "At your service!",
              "Hey, what can I do for you?"]
failure_text = ["Sorry didn't get you!",
                "Sorry, can't do that yet!",
                "I don't know what to do!",
                "Naah! not one of my skills",
                "Sorry, but my powers are limited..."]
goodbye_text = ["See you later mater!",
                "Hasta la Vista!",
                "Good day!",
                "Adios amigo!",
                "See you soon!"]

the_voice.say_and_print("Hey user, what should I call you?")
while True:
    try:
        fnm = the_voice.listening()
        fnm.lower()
        if fnm == "cancel":
            break
        user_name = fnm
        break
    except:
        print("Please say the name again!")
        print("or Say \"CANCEL\" to cancel")
asst_nm = "Dora"  #by default

try:
    the_voice.say_and_print("Hello " + user_name)
except:
    the_voice.say_and_print("Hello!")
the_voice.say_and_print("Starting, Please wait...")
# on_startup()  # this function takes some time, it reads current processes and looks for any new directory
the_voice.say_and_print(random.choice(greet_text))
cmd = the_voice.wake_listen(asst_nm)
try:
    cmd = cmd.lower()
except:
    cmd = None
while True:
    if cmd is None:
        pass
    elif asst_nm in cmd or "doora" in cmd or "hello" in cmd:
        the_voice.say("yes"+user_name)
        cmd = the_voice.listening()
        try:
            cmd = cmd.lower()
        except:
            cmd = None

        if cmd is None:
            pass

        elif ("change" in cmd and "profile" in cmd) or ("change" in cmd and "user" in cmd):
            the_voice.say_and_print("What is the first name of user?")
            while True:
                fnm = the_voice.listening()
                try:
                    fnm.lower()
                    if fnm == "cancel":
                        break
                    user_name=fnm
                    break
                except:
                    print("Please say the name again!")
                    print("or Say \"CANCEL\" to cancel")
        elif ("change" in cmd and "assistant" in cmd) or ("load" in cmd and "assistant" in cmd) or (
                "assistant" in cmd and "profile" in cmd):
            the_voice.say_and_print("Tell the name of assistant you want to use?")
            name = the_voice.listening()
            while True:
                try:
                    name = name.lower()
                    if name == "cancel":
                        break
                    else:
                        asst_nm = name
                        
                        the_voice.say_and_print("Assistant profile successfully loaded!")
                        try:
                            the_voice.say_and_print("Hello " + user_name)
                        except:
                            the_voice.say_and_print("Hello!")
                        break
                except:
                    print("Please Enter a name or \"CANCEL\" to cancel")
                    name = input(">>>")
        elif main_harshsit.start(cmd):
            pass
        elif main_archit.start(cmd):
            pass
        elif "exit" in cmd or "terminate" in cmd or ("shut" in cmd and "down" in cmd) or "stop" in cmd or (
                "good" in cmd and "bye" in cmd) or "see you later" in cmd or ("turn" in cmd and "off" in cmd):
            the_voice.say_and_print(random.choice(goodbye_text))
            break
        else:
            the_voice.say_and_print(random.choice(failure_text))
            the_voice.say_and_print("Please try any other command...")

    else:
        pass
    cmd = the_voice.wake_listen(asst_nm)
    try:
        cmd = cmd.lower()
    except:
        cmd = None
