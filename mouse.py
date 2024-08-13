import pyautogui
import time

# Define the interval (in seconds)
interval = 60

try:
    count = 0
    while True:
        # Get the current mouse position
        x, y = pyautogui.position()
        
        # Move the mouse cursor down by 1 pixel
        pyautogui.moveTo(x, y + 5)
        
        # Wait for the specified interval
        time.sleep(interval)

        count += 1

except KeyboardInterrupt:
    print("Script stopped by user.")
