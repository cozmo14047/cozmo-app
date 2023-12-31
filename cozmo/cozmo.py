import tkinter
from tkinter import Tk, Scale, Label
import tkinter as tk
import pycozmo
import time
from PIL import ImageTk, Image
logo_path = "logo.jpg"
# Connect to Cozmo

# Define minimum and maximum lift height
MIN_LIFT_HEIGHT = pycozmo.robot.MIN_LIFT_HEIGHT.mm
MAX_LIFT_HEIGHT = pycozmo.robot.MAX_LIFT_HEIGHT.mm

def update_lift_height(new_height):
    global current_lift_height
    current_lift_height = new_height
    cli.set_lift_height(current_lift_height)
   
    # Update label to show current lift height
    

root = tkinter.Tk()
root.title("Cozmo")
root.configure(bg="#5f5e5f")
root.geometry("400x300")
    
image = Image.open(logo_path)
resized_image = image.resize((550, 100))
tk_image = ImageTk.PhotoImage(resized_image)
logo_label = tkinter.Label(root, image=tk_image)
logo_label = tk.Label(root, image=tk_image, bd=0)
logo_label.pack()
image_label = tk.Label(root)
image_label = tk.Label(root, image=tk_image, bd=0)
image_label.pack()

lift_slider = Scale(root, from_=MIN_LIFT_HEIGHT, to_=MAX_LIFT_HEIGHT, orient="vertical",
                    command=update_lift_height, bg="black",troughcolor="#000000",fg="#ffffff",highlightthickness=0)
lift_slider.pack(side=tk.RIGHT, fill=tk.Y)
lift_slider.pack()
def on_camera_image(cli, new_im):
    """Handle new images from the robot."""
    global last_im, image_label
    last_im = new_im

    if last_im:
        # Process image for display in Tkinter
        im = last_im.convert('RGB')  # Convert to RGB before resizing
        im = im.resize((550, 300))  # Resized for compatibility
        photo = ImageTk.PhotoImage(image=im)

        # Update the image in the label
        image_label.config(image=photo)
        image_label.image = photo  # Keep a reference to avoid garbage collection

with pycozmo.connect() as cli:
    time.sleep(1)
    angle = (pycozmo.robot.MAX_HEAD_ANGLE.radians - pycozmo.robot.MIN_HEAD_ANGLE.radians) / 2.0
    cli.set_head_angle(angle)
    time.sleep(1)
    # Set initial lift height
    current_lift_height = MIN_LIFT_HEIGHT
    update_lift_height(current_lift_height)
    cli.set_volume(50000)

    # A 22 kHz, 16-bit, mono file is required.
    cli.play_audio("hello.wav")
    cli.wait_for(pycozmo.event.EvtAudioCompleted)
    cli.add_handler(pycozmo.event.EvtNewRawCameraImage, on_camera_image)
    cli.enable_camera()
    
    min_angle = pycozmo.robot.MIN_HEAD_ANGLE.radians
    max_angle = pycozmo.robot.MAX_HEAD_ANGLE.radians

    def update_angle_label():
        
       current_angle = cli.get_head_angle().radians
       doubled_angle = 2 * current_angle
       current_angle_label.config(text=f"Current Head Angle: {float(doubled_angle):.2f}")

    head_angle_slider = tk.Scale(
        root,
        from_=min_angle,
        to=max_angle,
        orient=tk.VERTICAL,
        resolution=0.01,
        command=lambda angle: (cli.set_head_angle(angle), update_angle_label()),
         troughcolor="#000000",  # Sets background color of the slider
         bg="#000000",  # Sets background color of the slide bar
         fg="#ffffff",  # Sets the color of the slider knob and tick marks
         highlightthickness=0,
    )
    head_angle_slider.pack(side=tk.LEFT, fill=tk.Y)

    head_angle_slider.pack()
    last_im = None
    
  
    root.mainloop()
