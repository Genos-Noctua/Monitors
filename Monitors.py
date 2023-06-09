#Monitors 2.5
import os, time
from PIL import Image
from pystray import Icon, Menu as menu, MenuItem as item

def switch(mode):
    os.system('.\MultiMonitorTool.exe /SetPrimary 3CM72807W7')
    if mode == "1":
        os.system('.\MultiMonitorTool.exe /disable HS2P706501 QPC073601733')
        os.system('.\MultiMonitorTool.exe /LoadConfig "1configs"')
    elif mode == "2":
        os.system('.\MultiMonitorTool.exe /disable QPC073601733')
        os.system('.\MultiMonitorTool.exe /enable HS2P706501')
        os.system('.\MultiMonitorTool.exe /LoadConfig "2configs"')
    elif mode == "3":
        for x in range(3):
            os.system('.\MultiMonitorTool.exe /LoadConfig "3configs"')
            time.sleep(0.1)
    elif mode == "TV":
        os.system('.\MultiMonitorTool.exe /LoadConfig "TVconfigs"')
    with open("state", "w+") as f:
        print(mode, file=f, end="")

def main():
    if not os.path.isfile("state"):
        with open("state", "w+"): pass
    with open("state", "r") as file:
        mode = file.read()
        switch(mode)
    with Image.open("Monitor.ico") as f:
        icon = Icon("Monitors", f, menu=menu(item("1", lambda: switch("1")), item("2", lambda: switch("2")), item("3", lambda: switch("3")), item("TV", lambda: switch("TV"))))
        icon.run()

if __name__ == "__main__":
    main()