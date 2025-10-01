import pyautogui
import pyperclip
import time
from openai import OpenAI
client = OpenAI(api_key="<your_api_key>")
time.sleep(3)
def is_last_message_from_Sender_name(chat_log,sender_name="Ss"):
    messages=chat_log.strip().split("/2025] ")[-1]
    if sender_name in messages:
        return True
    return False
# Small delay before script starts (so you can switch to the right window)
pyautogui.moveTo(705, 1070, duration=0.5)

    
    
while True:
    # Step 2: Drag from (687, 247) to (1845, 889)
    pyautogui.moveTo(707, 248, duration=0.5)
    pyautogui.dragTo(786, 1005, duration=1, button='left')

        # Step 3: Copy to clipboard (Ctrl + C)
    pyautogui.hotkey("ctrl", "c")
    pyautogui.click(722,270)

    time.sleep(0.5)

   
    chat_history = pyperclip.paste()

    
    print("Copied Text:\n", chat_history)
    #print(is_last_message_from_Sender_name(chat_history))

    if is_last_message_from_Sender_name(chat_history):

        response = client.chat.completions.create(
            model="gpt-4o-mini",   # you can also use "gpt-4.1" or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are person named priyanka who speaks  english.you are from india.You analyze chat history and  respond  like priyanka.Output should be next chat response(text message only)."},
                {"role": "user", "content": chat_history}
            ]
        )



        reply=response.choices[0].message.content
        print(reply)
        clean_reply=reply.strip()
        pyperclip.copy(clean_reply)

        pyautogui.click(842, 977)


        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)
        pyautogui.press("enter")
        
