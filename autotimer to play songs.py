import time
import webbrowser
i=0
a=int(input("Enter number of times you want to play songs"))
b=int(input("Enter interval if time in sec after you want to play song"))
while(i<=a):
    time.sleep(b);
    webbrowser.open("https://music.youtube.com/watch?v=bK3lslhN458&list=RDAMVMbK3lslhN458")
    i+=1
