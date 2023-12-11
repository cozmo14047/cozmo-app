import tkinter

# Import Py Cozmo
from pycozmo import *

# Connect to Cozmo
cozmo = connect()

# Initialize Tkinter
root = tkinter.Tk()
root.title("Cozmo")
root.configure(bg="black")
root.geometry("400x300")

# Label with message
message_label = tkinter.Label(
    root, text="Please ensure you are connected.", fg="white", bg="black"
)
message_label.pack()

# Button to raise head
raise_head_button = tkinter.Button(root, text="Raise Head", command=cozmo.move_head, args=(50, 0.5))
raise_head_button.pack()

# Button to lower head
lower_head_button = tkinter.Button(root, text="Lower Head", command=cozmo.move_head, args=(-50, 0.5))
lower_head_button.pack()

# Start main loop
root.mainloop()

# Disconnect from Cozmo
cozmo.disconnect()
