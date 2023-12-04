import ctypes
from pynput import keyboard
import time
stop_mouse_movement = False 
dmr=False
mouse_stat=1
def set_mouse_stat(dec):
    global mouse_stat
    mouse_stat=dec
def move_mouse(coordinates):


    global stop_mouse_movement,dmr
    stop_mouse_movement = False
    start_time2 = time.time()
    
    for coord_type in ["special", "dmr", "default"]:
        if coord_type in coordinates:
            if coord_type == "dmr":
                dmr=True
            for coordinate in coordinates[coord_type]:
                duration, delay, vertical = coordinate
                vertical = round(vertical * mouse_stat)     
                start_time = time.time()
                end_time = start_time + duration
                if not stop_mouse_movement:
                    print("Giá trị bây giờ: ",coord_type,": (",duration,",",delay,",",vertical,")")
                
                while time.time() < end_time and not stop_mouse_movement:
                    if coord_type == "special":
                        ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0, 0)          
                    ctypes.windll.user32.mouse_event(0x0001, 0, vertical, 0, 0)
                    
                    time.sleep(delay)
            
    elapsed_time = time.time() - start_time2
    print(f"Thời gian đã trôi qua: {elapsed_time} giây")


            
def stop(value):
    global stop_mouse_movement, dmr
    if value=="dmr":
        dmr=False
        stop_mouse_movement = True
    if value=="ar" and not dmr:
        stop_mouse_movement = True

