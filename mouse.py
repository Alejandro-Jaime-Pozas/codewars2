import pyautogui
import time

# Define the interval (in seconds)
interval = 2

try:
    count = 0
    n = 0
    while True:
        # Get the current mouse position
        x, y = pyautogui.position()
        
        # Move the mouse cursor down by 1 pixel
        if n == 0:
            pyautogui.moveTo(x, y + 250)
            n = 1
        elif n == 1:
            pyautogui.moveTo(x, y + -250)
            n = 0

        
        # Wait for the specified interval
        time.sleep(interval)

        count += 1

except KeyboardInterrupt:
    print("Script stopped by user.")
