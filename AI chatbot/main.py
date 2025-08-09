import pyautogui
import time
import pyperclip
import openai


time.sleep(2)


pyautogui.click(x=1238, y=1177)
time.sleep(1)  


pyautogui.moveTo(667, 233)
pyautogui.mouseDown()  
pyautogui.moveTo(1880, 1407, duration=0.5)  
pyautogui.mouseUp()  
time.sleep(1)


pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)  # Wait for the copy to complete
pyautogui.click(670,243)

chat_history = pyperclip.paste()
print("Copied text:", chat_history)

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content":"You are a person name Yad who speaks marathi"},
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
