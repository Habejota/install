from os import system, getcwd
from time import sleep
from random import randint

pwd = getcwd()

print("Preparing Setup Installer. . ."), sleep(randint(2, 5))
print("mirror: https://github.com/TenayaOS/OSystem.git \n")
print("Instruction:")
print("=================================================")
print(f"After donwload files you need entrace in {pwd} and ")
print("to copy all files in folder OSystem and you active")
print("show ocults files and copy all files and floders in ")
print("diretory \os don't delete any file!")
print("=================================================")
input("PRESS ENTER TO SET UP INSTALATION. . .")
print("Time connection: 3/ms baud: 7900")
print("NServer: https://github.com/")
system("git clone https://github.com/TenayaOS/OSystem.git")
print("Download complet!")
print("The computer be roboot, you need eject this drive CD-Rom"), sleep(2.84)
input("PRESS ENTER to reboot Tenaya. . .")