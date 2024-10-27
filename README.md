# Automated YouTube Viewer Script

This Python script automates the task of opening YouTube videos in Google Chrome's Guest mode, visiting each specified URL, and interacting with certain screen elements through image recognition. Primarily, this script is intended for automating YouTube video views by playing each video link for a specified number of repetitions. Once the video reaches the end screen, the script closes the browser window, reopening it to play the next video. 

## Features
- Opens Google Chrome in Guest mode, ensuring a fresh session for each view (no cookies or history).
- Visits the URLs provided by the user to play each YouTube video.
- Uses image recognition to detect and click specific screen elements, such as the play button.
- Closes the browser window upon detecting the video’s end screen and repeats the process for the defined number of cycles.

## Requirements

1. **Python Modules**:
   - `pyautogui`: For controlling mouse, keyboard, and locating images on the screen.
     - Install using `pip install pyautogui`.
   - `os` and `time`: Standard Python libraries for file handling and managing delays (pre-installed).

2. **Required Files**:
   - `play.png`, `endscreen.png`, and `endscreen2.jpg`: Images used to recognize and interact with specific elements on YouTube.
     - These files must be placed in the same folder as this script.
   - `chromeguest.lnk`: A shortcut to Google Chrome that opens the browser in Guest mode.
     - Place this shortcut on your Desktop.
     - **To configure this shortcut**: Right-click the Chrome shortcut, select **Properties**, and add `--guest` to the end of the **Target** field to open Chrome in Guest mode each time.

## Setup Instructions

1. **Download and Prepare Image Files**:
   - Ensure that `play.png`, `endscreen.png`, and `endscreen2.jpg` match the on-screen YouTube elements for the play button and the end screen. These images enable the script to locate these elements accurately using `pyautogui`.

2. **Configure Chrome Shortcut for Guest Mode**:
   - Locate or create a Chrome shortcut on your Desktop.
   - Right-click the shortcut, select **Properties**, and append `--guest` to the end of the **Target** field.
   - Click **OK** to save.

3. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the folder containing the script, then run:
     ```bash
     python your_script_name.py
     ```
   - Follow the prompts to specify the number of repetitions and the list of YouTube URLs.

## Usage

Upon running the script:
1. You will be prompted to enter the number of repetitions and the list of YouTube URLs.
2. The script will launch Chrome in Guest mode, navigate to each URL, attempt to click the play button using `play.png`, and start the video.
3. Once the video ends (detected using `endscreen.png` or `endscreen2.jpg`), the script closes the browser window.
4. This process will repeat for the specified number of cycles.

## Notes

- **Image Accuracy**: Ensure that `play.png`, `endscreen.png`, and `endscreen2.jpg` are clear and closely match the appearance of YouTube’s play and end-screen elements. `pyautogui` relies on image similarity to locate and interact with these elements.
- **Wait Times**: The script includes a 1-second delay between actions to handle page loading times. Adjust the delay if you encounter timing issues.

## Troubleshooting

- If the script fails to detect elements, verify that `play.png`, `endscreen.png`, and `endscreen2.jpg` are accurate screenshots of the relevant on-screen YouTube buttons.
- **Common Errors**:
   - `pyautogui.ImageNotFoundException`: Occurs if `pyautogui` cannot locate an image on the screen. Ensure your images are stored in the correct location and are clear for accurate detection.

## Disclaimer

This script is provided for educational purposes only. Use responsibly, ensuring compliance with YouTube’s terms of service and automated interactions policies.
