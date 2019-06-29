import datetime, os, sys, win32api

def linuxSetTime():
    password = "" #set your password here
    osTime = datetime.datetime.now().time().isoformat()
    currentTime = str(int(osTime[:2]) - 3) + osTime[2:]
    command = 'date -s ' + currentTime
    os.popen("sudo -S %s"%(command), 'w').write(password)

def winSetTime():
    osTime = win32api.GetSystemTime()
    osTime[5] += 3
    win32api.SetSystemTime(*osTime)

if sys.platform.startswith('linux2'):
    linuxSetTime()
else:
    winSetTime()
