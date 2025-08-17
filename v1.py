import pyautogui
import time
import csv
import pyperclip

with open("usn.csv",mode="a",newline="") as file:
    writer= csv.DictWriter(file,fieldnames=["USN","SGPA"])
    
    time.sleep(5)

    for i in range(75,97):

        
        pyautogui.click(x=1304, y=442)
        pyautogui.typewrite(f"1WN24CS{str(i).zfill(3)}")
        pyautogui.click(x=1290, y=658)
        time.sleep(5)
        pyautogui.moveTo(x=1151, y=670)
        pyautogui.click(x=1151, y=670,clicks=2)
        time.sleep(5)
        pyautogui.click(x=1022, y=731,clicks=2)
        pyautogui.hotkey("ctrl","c")
        pyautogui.click(x=27, y=67,clicks=2)

        sgpa=pyperclip.paste()

        writer.writerow({ "USN":f"1BF24CS{str(i).zfill(3)}",
                         "SGPA": sgpa })

        time.sleep(2)
        pyautogui.click(x=1304, y=442,clicks=2)
        pyautogui.hotkey("delete")