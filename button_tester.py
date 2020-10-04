from gpiozero import Button
button = Button(7)

button.wait_for_press()
print("Button was pressed")
