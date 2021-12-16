# from pynput.keyboard import Key, Controller

# keyboard = Controller()

# Press and release space
# keyboard.press(Key.space)
# keyboard.release(Key.space)

# # Type a lower case A; this will work even if no key on the
# # physical keyboard is labelled 'A'
# keyboard.press('a')
# keyboard.release('a')

# # Type two upper case As
# keyboard.press('A')
# keyboard.release('A')
# with keyboard.pressed(Key.shift):
#     keyboard.press('a')
#     keyboard.release('a')

# # Type 'Hello World' using the shortcut type method
# keyboard.type('Hello World')
from pynput import keyboard
def key_recognizer():
    outputArray = []
    def on_press(key):  
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
            outputArray.append(("press",key))
        except AttributeError:
            print('special key {0} pressed'.format(
                key))
                # repair this code, to return something more meaningfull
            outputArray.append(("press",key))

    def on_release(key):
        print('{0} released'.format(
            key))
        outputArray.append(("release",key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()
    return outputArray