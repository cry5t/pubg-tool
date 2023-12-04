import win32gui, time
import config
from pynput.mouse import Listener
import threading
import win32con

stop_drawing = False



def drawing():
    while not stop_drawing:
        x=config.x // 2  
        y=config.y // 2  
        
        
        white_color = (255, 255, 255)  # Sử dụng tuple cho màu trắng

        # Rút trích các kênh màu
        red, green, blue = white_color

        # Tạo màu 32-bit từ các kênh màu bằng cách sử dụng bit shifting và OR logic
        color = (red << 16) | (green << 8) | blue
        
        
        hwnd=win32gui.WindowFromPoint((x,y))
        hdc=win32gui.GetDC(hwnd)
        x1,y1=win32gui.ScreenToClient(hwnd,(x,y))

        win32gui.SetPixel(hdc, x1, y1, color)
        for i in range(20, 60):
            win32gui.SetPixel(hdc, x1 - i, y1, color)
            win32gui.SetPixel(hdc, x1 + i, y1, color)
            win32gui.SetPixel(hdc, x1, y1 - i, color)
            win32gui.SetPixel(hdc, x1, y1 + i, color)
        for i in range(1, 4):
            win32gui.SetPixel(hdc, x1 - i, y1, color)
            win32gui.SetPixel(hdc, x1 + i, y1, color)
            win32gui.SetPixel(hdc, x1, y1 - i, color)
            win32gui.SetPixel(hdc, x1, y1 + i, color)
        for i in range(1, 3):
            win32gui.SetPixel(hdc,x1-i,y1-i,color)
            win32gui.SetPixel(hdc,x1+i,y1+i,color)
            win32gui.SetPixel(hdc,x1-i,y1+i,color)
            win32gui.SetPixel(hdc,x1+i,y1-i,color)
        win32gui.ReleaseDC(hwnd, hdc)         
        time.sleep(0.004)
def start_drawing():
    global stop_drawing
    stop_drawing = False
    drawing()


def stop():
    global stop_drawing
    stop_drawing = True  



def on_click(x, y, button, pressed):
    if button == button.right:
        if pressed:
            stop()
        else:
            thread = threading.Thread(target=start_drawing)
            thread.start()

# Tạo một lắng nghe chuột
with Listener(on_click=on_click) as listener:
    listener.join()
