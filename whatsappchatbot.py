import google.generativeai as genai
import pyautogui
import pyperclip
import time


API_KEY = "Enter You API key here"
genai.configure(api_key=API_KEY)


persona = "You are Yadnesh, who speaks Hindi, English, and is a coder."
model = genai.GenerativeModel("gemini-2.5-flash")
chat = model.start_chat(
    history=[
        {"role": "user", "parts": persona}   
    ]
)

print("✅ Chatbot ready! Type 'exit' in WhatsApp to quit.")

previous_text = None   
max_retries = 1       
retry_interval = 2     
timeout_retries = 0  

# ====== MAIN LOOP ======
while True:
    time.sleep(2)

   
    pyautogui.click(x=1327, y=1168)     
    time.sleep(1)
    pyautogui.moveTo(667, 233)
    pyautogui.mouseDown()
    pyautogui.moveTo(1880, 1407, duration=0.5)
    pyautogui.mouseUp()
    time.sleep(1)

    
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    chat_history = pyperclip.paste().strip()

    if chat_history.lower() == "exit":
        print(" Exiting chat...")
        break

    if chat_history != previous_text and chat_history != "":
        previous_text = chat_history
        timeout_retries = 0

        print(f"\n[ Copied] {chat_history}")

        # --- Gemini Reply ---
        try:
            response = chat.send_message(chat_history)

            # Extract text safely
            reply_text = None
            if hasattr(response, "text") and response.text:
                reply_text = response.text
            elif hasattr(response, "candidates") and response.candidates:
                try:
                    reply_text = response.candidates[0].content.parts[0].text
                except Exception as e:
                    print("⚠️ Failed to extract reply:", e)

            if not reply_text:
                reply_text = "(No reply received from Gemini)"

            print(f"[ Gemini] {reply_text}")

           
            pyperclip.copy(reply_text)
            pyautogui.click(x=1613, y=1098)  
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.5)
            pyautogui.press('enter')

        except Exception as e:
            print("❌ Error while calling Gemini:", e)

    else:
       timeout_retries += 1
       print("⚠️ No new text detected. Exiting...")

       break
