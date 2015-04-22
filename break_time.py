import time
import webbrowser

totalBreaks = 3
breakCount = 0

print ("This program started on " + time.ctime())
while(breakCount < totalBreaks):
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=j9g3uUsQi2s")
    breakCount += 1
