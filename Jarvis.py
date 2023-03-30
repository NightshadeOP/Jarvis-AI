import time
import webbrowser
print("hello i am jarvis ")
z=int(input("how many websites do you want me to open ? "))
time.sleep(1)
for i in range(z):
    q=input("which website should i open ? : ")
    time.sleep(3)
    webbrowser.open(f"www.{q}.com")

