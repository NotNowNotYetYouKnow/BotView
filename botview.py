import os
import pyautogui
import time
pyautogui.FAILSAFE=False

def see_and_click(image_path, confidence=0.8, wait_time=1, max_attempts=None):

    attempts = 0
    while max_attempts is None or attempts < max_attempts:
        try:
            image_location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
            if image_location is not None:
                pyautogui.click(image_location)
                return True  # Image found and clicked
        except pyautogui.ImageNotFoundException:
            print(f"Image not found. Retrying ({attempts+1}/{max_attempts})...")
            time.sleep(wait_time)
            attempts += 1
    print(f"Maximum attempts reached. Image not found: {image_path}")
    return False  # Image not found after maximum attempts

def main():

    r = int(input("How many times do you wish to repeat?"))
    l = 1
    links = []
    n = int(input("Enter number of links: "))

    for i in range(0, n):
        ele = str(input())
        links.append(ele)

    while l <= r:
        os.startfile(r"C:\Users\schoo\Desktop\chromeguest.lnk")
        time.sleep(1)

        for i in range(0, len(links)):
            pyautogui.write(links[i])
            pyautogui.hotkey('enter')

            while True:
                 # Keep checking for "play.png" without any limit
                # Check for "endscreen" or "endscreen2" and break if found
                if see_and_click(r"C:\Users\schoo\Desktop\Projects\BotView\play.png", confidence=0.8, max_attempts=None):
                    time.sleep(1)
                    continue
                if see_and_click(r"C:\Users\schoo\Desktop\Projects\BotView\endscreen.png", confidence=0.75, max_attempts=None) or \
                    see_and_click(r"C:\Users\schoo\Desktop\Projects\BotView\endscreen2.jpg", confidence=0.75, max_attempts=None):
                    pyautogui.keyDown('alt')
                    pyautogui.press('f4')  # Press the 'F4' key
                    pyautogui.keyUp('alt')
                    break
   
        l += 1

if __name__ == "__main__":
    main()
  
