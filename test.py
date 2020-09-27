import pyautogui
import time
import keyboard



#definition 
pyautogui.FAILSAFE = False

while True:
    if keyboard.is_pressed("F8"):    
        # 좌표저장 
        x,y = pyautogui.position()
        # 클릭
        pyautogui.click(x, y)

        write_btn = pyautogui.locateCenterOnScreen('write.png',confidence=0.7)
        
        #for x in range(0, 25):
        # 복사
        pyautogui.hotkey('ctrl', 'c')
        # 붙여넣기 로직 (텔레그램)
        pyautogui.click(write_btn[0],write_btn[1])
            # write button click
        pyautogui.moveTo(10,10)

        time.sleep(1)
        add_btn = pyautogui.locateCenterOnScreen("add.png",confidence=0.85)


        for x in range(0, 25):       
                # add button search
            pyautogui.click(add_btn[0],add_btn[1])
                # add button click
            time.sleep(1)
            pyautogui.hotkey("ctrl","v")
                # name input
            time.sleep(0.2)
            pyautogui.press("down")
            pyautogui.press("down")
            pyautogui.press("down")
            time.sleep(0.2)
            pyautogui.hotkey("ctrl","v")
            time.sleep(0.2)

            if x == 0:
                check_btn = pyautogui.locateCenterOnScreen("check.png",confidence=0.85)
            pyautogui.click(check_btn[0],check_btn[1])
            time.sleep(1.5)


            invite_btn = pyautogui.locateCenterOnScreen("invite.png",confidence=0.85)
            
            if invite_btn:
                pyautogui.click(invite_btn[0], invite_btn[1])
                time.sleep(0.5)
            
            

            if x == 0:
                prev_btn = pyautogui.locateCenterOnScreen("arrow.png",confidence=0.85)
            pyautogui.click(prev_btn[0], prev_btn[1])
            time.sleep(0.5)
            pyautogui.click(50,250)
            time.sleep(0.2)
            if x != 24:
                pyautogui.press("down")
                pyautogui.hotkey("ctrl","c")
        pyautogui.click(prev_btn[0],prev_btn[1])
   

