import mou
from pynput import mouse
import threading
from pynput import keyboard
import config
import importlib
import skill
import time
from state import MyState
my_state = MyState()
my_state.set_data1("none")
my_state.set_data2("none")

last_release_time = 0
click_event_in_progress = False
left_pressed = False
right_pressed = False
both_pressed = False
now_gun_is_sniper = False
snipers_mapping = config.snipers_mapping
dev=config.dev
guns_mapping = config.guns_mapping
coordinates = config.coordinates
sniper_coordinates = config.sniper_coordinates
tap_button = config.tap_button
spray_button = config.spray_button

def update_config(options):
    global guns, guns_mapping, coordinates
    importlib.reload(config)
    if options == "coordinates":
        coordinates = config.coordinates
def on_click(x, y, button, pressed):
    global left_pressed, right_pressed, both_pressed, now_gun_is_sniper, click_event_in_progress, last_release_time
    
    if not both_pressed:
        if button == mouse.Button.left:
            if pressed and not click_event_in_progress:

                current_time = time.time()
                time_since_release = current_time - last_release_time
                if time_since_release > 0.002:
                    click_event_in_progress = True
                    left_pressed = True
                last_release_time=0
            elif not pressed:
                click_event_in_progress = False
                left_pressed = False
            
        elif button == mouse.Button.right:
            right_pressed = pressed
            if not pressed:
                right_pressed = False

                
    if left_pressed and right_pressed:
        if not both_pressed:
            both_pressed = True
            mou.stop("dmr")
            if not now_gun_is_sniper  and dev:
                update_config("coordinates")
                thread = threading.Thread(target=mou.move_mouse, args=(coordinates,))
            elif not now_gun_is_sniper:
                
                print(f"Now gun: ",my_state.get_data1())
                thread = threading.Thread(target=mou.move_mouse, args=(coordinates,))
            elif now_gun_is_sniper:
                print(f"Now gun: ",my_state.get_data2())  
                thread = threading.Thread(target=mou.move_mouse, args=(sniper_coordinates,))               
            thread.start()

def on_click_released(x, y, button, pressed):
    global both_pressed, last_release_time, click_event_in_progress
    if button == mouse.Button.right:
        if not pressed:
            mou.stop("dmr")
            both_pressed=False
            click_event_in_progress = False
            last_release_time = time.time()
    elif button == mouse.Button.left or button == mouse.Button.right:
        if not pressed:
            mou.stop("ar")
            both_pressed=False
            click_event_in_progress = False
            last_release_time = time.time()
            

pressed_keys = set()

def on_key_press(key):
    global now_gun_is_sniper, coordinates, sniper_coordinates
    
    try:
        pressed_keys.add(key.char)
        found_gun = None
        found_mapping = None

        for mapping in [guns_mapping, snipers_mapping]:
            for combo, (gun, coords) in mapping.items():
                if all(k in pressed_keys for k in combo):
                    
                    found_gun = gun
                    found_mapping = mapping
                    break

            if found_gun:
                print(found_gun)
                break

        if found_mapping:
            if found_mapping is guns_mapping:
                coordinates = coords
                my_state.set_data1(found_gun)

            elif found_mapping is snipers_mapping:
                sniper_coordinates = coords
                my_state.set_data2(found_gun)    

        if key.char in spray_button:
            now_gun_is_sniper = False
            for combo, (gun, _) in sorted(guns_mapping.items()):
                print(f'{combo[0]} + {combo[1]} = {gun}')
            print("_______________________<",my_state.get_data1() ,">_________________________")
            print("Sprayyyy!!!!")
        elif key.char in tap_button:
            now_gun_is_sniper = True
            for combo, (gun, _) in sorted(snipers_mapping.items()):
                print(f'{combo[0]} + {combo[1]} = {gun}')
            print("_______________________<",my_state.get_data2() ,">_________________________")
            print("Tap tap tappp!!!!")
        if dev:
            print("on dev mode")
        #print(pressed_keys)
    except Exception as e:
        pass

def on_key_release(key):
    try:
        if hasattr(key, 'char'):
            # Remove printable keys from the set
            pressed_keys.clear()

    except AttributeError:
        pass



def main():
    if dev:
        print("on dev mode")
    keyboard_listener = keyboard.Listener(
        on_press=on_key_press, 
        on_release=on_key_release
    )
    keyboard_listener.start()

    skill_listener = keyboard.Listener(
        on_press=skill.on_key_press, 
        on_release=skill.on_key_release
    )
    skill_listener.start()

    listener_pressed = mouse.Listener(on_click=on_click)
    listener_released = mouse.Listener(on_click=on_click_released)

    # Bắt đầu lắng nghe sự kiện chuột cho cả hai listener
    listener_pressed.start()
    listener_released.start()

    # Giữ chương trình chạy
    listener_pressed.join()
    listener_released.join()


if __name__ == "__main__":
    main()
    
