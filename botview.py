import os
import pyautogui
import time

pyautogui.FAILSAFE = False

def see_and_click(image_path, confidence=0.8, wait_time=1, max_attempts=None):
    attempts = 0
    while max_attempts is None or attempts < max_attempts:
        try:
            image_location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
            if image_location is not None:
                pyautogui.click(image_location)
                return True  # Image found and clicked
        except pyautogui.ImageNotFoundException:
            print(f"Image not found. Retrying ({attempts + 1}/{max_attempts})...")
            time.sleep(wait_time)
            attempts += 1
    print(f"Maximum attempts reached. Image not found: {image_path}")
    return False  # Image not found after maximum attempts

def open_browser_and_click_links(links, repeat_count):
    for _ in range(repeat_count):
        os.startfile(os.path.join(os.path.expanduser("~"), "Desktop", "chromeguest.lnk"))
        time.sleep(2)  # Increase wait time to ensure browser loads completely

        for link in links:
            pyautogui.write(link)
            pyautogui.hotkey('enter')

            while True:
                if see_and_click(os.path.join(os.path.dirname(__file__), "play.png"), confidence=0.8):
                    time.sleep(1)  # Wait for the next action
                    continue
                
                if (see_and_click(os.path.join(os.path.dirname(__file__), "endscreen.png"), confidence=0.75) or
                    see_and_click(os.path.join(os.path.dirname(__file__), "endscreen2.jpg"), confidence=0.75)):
                    pyautogui.keyDown('alt')
                    pyautogui.press('f4')  # Close the browser window
                    pyautogui.keyUp('alt')
                    break

def main():
    repeat_count = int(input("How many times do you wish to repeat? "))
    link_count = int(input("Enter number of links: "))
    links = [input(f"Enter link {i + 1}: ") for i in range(link_count)]

    open_browser_and_click_links(links, repeat_count)

if __name__ == "__main__":
    main()
