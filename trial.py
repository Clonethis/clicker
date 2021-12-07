from pynput.mouse import Button, Controller


mouse = Controller()
nice=[[0,0]]
mouse.position=(10,20)
# mouse.position()
nice.append(mouse.position)
print("loaded" )
mouse.position=nice[0]
print("now jumped using load from array")
