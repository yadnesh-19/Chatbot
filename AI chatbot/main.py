import pyautogui
import time
import pyperclip
import openai

# Pause for 2 seconds before starting (gives you time to position your cursor)
time.sleep(2)

# 1: Click on the icon at (1238, 1177)
pyautogui.click(x=1238, y=1177)
time.sleep(1)  # Wait a moment after clicking

# 2: Drag from (667, 233) to (1880, 1407) to select text
pyautogui.moveTo(667, 233)
pyautogui.mouseDown()  # Press down the mouse button
pyautogui.moveTo(1880, 1407, duration=0.5)  # Move the mouse to the end position
pyautogui.mouseUp()  # Release the mouse button
time.sleep(1)

# 3: Copy the selected text (Ctrl+C)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)  # Wait for the copy to complete
pyautogui.click(670,243)
# 4: R
#etrieve the copied text from the clipboard
chat_history = pyperclip.paste()
print("Copied text:", chat_history)

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content":"You are a person name harry who speaks marathi"},
        {"role":"user","content":chat_history} 
    ]
)
response=(completion.choice[0].messages.content)
pyperclip.copy(response)
pyautogui.click(x=1613, y=1098)
time.sleep(0.5)

# 2. Paste the clipboard text
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)

# 3. Press Enter
pyautogui.press('enter')