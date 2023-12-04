from pynput import keyboard
import config
import mou
import time

skill_shift=config.skill_shift
keyboard_controller = keyboard.Controller()
caps_lock_pressed=False
last_call_time = 0  # Biến để lưu thời gian cuối cùng hàm press_c_once được gọi

def press_c_once():
    global last_call_time
    current_time = time.time()
    
    # Kiểm tra nếu đã đủ 1 giây kể từ lần gọi trước đó
    if current_time - last_call_time >= 0.3:
        keyboard_controller.press('c')
        keyboard_controller.release('c')
        last_call_time = current_time

def on_caps_lock_pressed():
    global caps_lock_pressed
    if not caps_lock_pressed:
        caps_lock_pressed = True
        mou.set_mouse_stat(1.7)
def on_caps_lock_released():
    global caps_lock_pressed
    caps_lock_pressed = False
    mou.set_mouse_stat(1)



def on_key_release(key):
    if key == keyboard.Key.caps_lock:
        on_caps_lock_released()


def on_key_press(key):
    global caps_lock_pressed
    if key == keyboard.Key.caps_lock:
        on_caps_lock_pressed()
    elif skill_shift and (key == keyboard.KeyCode.from_char('Q') or key == keyboard.KeyCode.from_char('E')):
        press_c_once()
