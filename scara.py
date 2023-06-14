import tkinter as tk
from tkinter import ttk
import serial

# Configure the serial connection
ser = serial.Serial('COM10', 9600)  # Change the port and baud rate to match your Arduino

# Function to send variables to Arduino
def send_variables(variable1, variable2, variable3):
    # Format the variables as a string separated by commas
    data = f"{variable1},{variable2},{variable3}"

    # Send the data to Arduino
    ser.write(data.encode())


# Function to handle toggle switch state change
def toggle_robot():
    if toggle_state.get():
        toggle_button.config(text="ON", style="Toggle.On.TButton")
        # Code to turn on the robot
    else:
        toggle_button.config(text="OFF", style="Toggle.Off.TButton")
        # Code to turn off the robot

# Function to handle reset button click
def reset_angles():
    send_variables(int(angle1_slider.get()), int(angle2_slider.get()), int(height_slider.get()))

# Function to update angle values
def update_angle_values(dummy):
    angle1_value.set(f"Angle 1: {angle1_slider.get():.1f} °")
    angle2_value.set(f"Angle 2: {angle2_slider.get():.1f} °")
    height_value.set(f"Hauteur: {height_slider.get():.1f} mm")

# Create the main window
root = tk.Tk()
root.title("SCARA Robot Control")
root.iconbitmap("icon.ico")  # Replace "path_to_icon_file.ico" with the actual path to your icon file

# Create a frame for the images and text
image_frame = ttk.Frame(root)
image_frame.pack(pady=10)

# Create image labels
image1 = tk.PhotoImage(file="enp.png", width=100, height=100)  # Replace "path_to_image1.png" with the actual path to your first image
image2 = tk.PhotoImage(file="icon.png", width=100, height=100)  # Replace "path_to_image2.png" with the actual path to your second image

image_label1 = ttk.Label(image_frame, image=image1)
image_label1.pack(side=tk.LEFT, padx=10)
text_label = ttk.Label(image_frame, text="  Ecole Nationale Polytechnique\n\n       Bras Robotique SCARA\n\n by Nacer Eddine BOUSSOUSSOU")
text_label.pack(side=tk.LEFT, padx=10)
image_label2 = ttk.Label(image_frame, image=image2)
image_label2.pack(side=tk.LEFT, padx=10)

# Create a frame for the sliders and buttons
control_frame = ttk.Frame(root)
control_frame.pack(pady=10)

# Create angle 1 slider and label
angle1_slider = ttk.Scale(control_frame, from_=0, to=180, length=200, command=update_angle_values)
angle1_slider.grid(row=0, column=0, padx=10)
angle1_value = tk.StringVar()
angle1_label = ttk.Label(control_frame, textvariable=angle1_value)
angle1_label.grid(row=0, column=1)

# Create angle 2 slider and label
angle2_slider = ttk.Scale(control_frame, from_=0, to=180, length=200, command=update_angle_values)
angle2_slider.grid(row=1, column=0, padx=10)
angle2_value = tk.StringVar()
angle2_label = ttk.Label(control_frame, textvariable=angle2_value)
angle2_label.grid(row=1, column=1)

# Create height slider and label
height_slider = ttk.Scale(control_frame, from_=0, to=6000, length=200, command=update_angle_values)
height_slider.grid(row=2, column=0, padx=10)
height_value = tk.StringVar()
height_label = ttk.Label(control_frame, textvariable=height_value)
height_label.grid(row=2, column=1)

# Create a frame for buttons
button_frame = ttk.Frame(control_frame)
button_frame.grid(row=3, column=0, columnspan=2, pady=10)

# Create the reset button
reset_button = ttk.Button(button_frame, text="Send", command=reset_angles)
reset_button.pack(side=tk.LEFT, padx=10)

# Create the toggle button
toggle_state = tk.BooleanVar()
toggle_button = ttk.Checkbutton(button_frame, text="Toggle", variable=toggle_state, command=toggle_robot)
#toggle_button.pack(side=tk.LEFT)

angle1_value.set(f"Angle 1: {angle1_slider.get():.1f}")
angle2_value.set(f"Angle 2: {angle2_slider.get():.1f}")
height_value.set(f"Height: {height_slider.get():.1f}")

# Start the Tkinter event loop
root.mainloop()
