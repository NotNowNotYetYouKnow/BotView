# Automated Browser Control Script

This Python script automates the task of opening Google Chrome in Guest mode, visiting specified URLs, and interacting with specific screen elements using image recognition. The script is helpful in scenarios where you need to automate repetitive actions across multiple web pages.

## Features
- Opens Google Chrome in Guest mode
- Visits URLs provided by the user
- Clicks specific elements based on image recognition
- Closes the browser window upon finding designated end-screen elements

## Requirements

1. **Python Modules**:
   - `pyautogui`: For controlling the mouse, keyboard, and locating images on the screen.
     - Install with `pip install pyautogui`.
   - `os` and `time`: Standard Python libraries (pre-installed).

2. **Required Files**:
   - `play.png`, `endscreen.png`, and `endscreen2.jpg`: Image files used to identify elements on the screen.
     - Place these files in the same folder as the script.
   - `chromeguest.lnk`: A shortcut to Google Chrome that opens the browser in Guest mode.
     - Place this shortcut on your Desktop.
     - **To configure this shortcut**: Right-click on the shortcut, select **Properties**, and add `--guest` to the end of the **Target** field to open Chrome in Guest mode each time the shortcut is used.

## Setup Instructions

1. **Download the Required Image Files**:
   - Ensure `play.png`, `endscreen.png`, and `endscreen2.jpg` match the on-screen buttons for "play" and "end screen" that the script should recognize and interact with.

2. **Configure Chrome Shortcut for Guest Mode**:
   - Locate or create a Chrome shortcut on your Desktop.
   - Right-click the shortcut, select **Properties**, and in the **Target** field, append `--guest` at the end.
   - Click **OK** to save.

3. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the script’s folder and run:
     ```bash
     python your_script_name.py
     ```
   - Follow the prompts to enter the number of repetitions and URLs you want the script to process.

## Usage

Upon running the script:
1. You will be prompted to enter the number of repetitions and the URLs.
2. The script will launch Chrome in Guest mode, visit each URL, click the play button (if found), and close the browser when the end screen is detected.
3. The process repeats based on the number of repetitions specified.

## Notes

- **Image Accuracy**: Ensure images used (play.png, endscreen.png, endscreen2.jpg) are clear and accurately reflect the on-screen buttons, as `pyautogui` relies on visual similarity to detect elements.
- **Wait Times**: The script includes a 1-second wait time between actions. You can adjust this to improve efficiency or handle delays in loading times.

## Troubleshooting

- If the script doesn’t detect elements on the screen, verify that `play.png`, `endscreen.png`, and `endscreen2.jpg` match the appearance and size of the buttons in your browser window.
- **Common Errors**:
   - `pyautogui.ImageNotFoundException`: This error occurs if `pyautogui` fails to locate an image. Ensure your images are clear and stored in the correct location.
  
## Disclaimer

This script is provided for educational purposes. Use responsibly and ensure compliance with terms of use and automated interactions policies for the websites you access.
