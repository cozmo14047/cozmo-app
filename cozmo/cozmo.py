import tkinter
import pycozmo
import time
from PIL import ImageTk, Image
logo_path = "logo.jpg"
# Connect to Cozmo
with pycozmo.connect() as cli:
    time.sleep(1)
    angle = (pycozmo.robot.MAX_HEAD_ANGLE.radians - pycozmo.robot.MIN_HEAD_ANGLE.radians) / 2.0
    cli.set_head_angle(angle)
    time.sleep(1)
      # Set volume to ~75%.
    cli.set_volume(50000)

    # A 22 kHz, 16-bit, mono file is required.
    cli.play_audio("hello.wav")
    cli.wait_for(pycozmo.event.EvtAudioCompleted)
    

    # Initialize Tkinter
    root = tkinter.Tk()
    root.title("Cozmo")
    root.configure(bg="#5f5e5f")
    root.geometry("400x300")
    
    image = Image.open(logo_path)
    resized_image = image.resize((550, 100))
    tk_image = ImageTk.PhotoImage(resized_image)
    logo_label = tkinter.Label(root, image=tk_image)
    logo_label.pack()

    # Label with message
    message_label = tkinter.Label(
        root, text="", fg="white", bg="#5f5e5f"
    )
    message_label.pack()

    # Button to raise head
    raise_head_button = tkinter.Button(
        root, text="Raise Head", command=lambda: cli.set_head_angle(angle + 0.4)
    )
    raise_head_button.pack()

    raise_lift_button = tkinter.Button(
        root, text="Raise lift", command=lambda: cli.set_lift_height(pycozmo.MAX_LIFT_HEIGHT.mm)
    )
    raise_lift_button.pack()



    lower_lift_button = tkinter.Button(
        root, text="lower lift", command=lambda: cli.set_lift_height(pycozmo.MIN_LIFT_HEIGHT.mm)
    )
    lower_lift_button.pack()
    


    # Button to lower head
    lower_head_button = tkinter.Button(
        root, text="Lower Head", command=lambda: cli.set_head_angle(angle - .8)
    )
    lower_head_button.pack()

    # Calculate head angles:
    angle = (pycozmo.robot.MAX_HEAD_ANGLE.radians - pycozmo.robot.MIN_HEAD_ANGLE.radians) / 2.0
    raise_angle = angle + 0.4  # 0.4 radians higher than neutral

    # Start main loop
    root.mainloop()

# Disconnect from Cozmo after tkinter closes
cli.disconnect()
