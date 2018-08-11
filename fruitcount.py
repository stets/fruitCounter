import subprocess, pexpect

child = pexpect.spawn ('nc challenges.kaizen-ctf.com 10001')
child.expect('\?')

def fruitFinder():
    fruitGrid = child.before
    fruit = fruitGrid[-4:]

    fruit = fruit.decode('utf-8')
    fruitGrid = fruitGrid.decode('utf-8')
    fruitCount = -1
    for each in fruitGrid:
        if fruit == each:
            fruitCount += 1
        else:
            pass
    return fruitCount

def answerSender(fruitCount):
    child.sendline(str(fruitCount))
    child.expect('\?')

timesRan = 0
while timesRan <= 1005:
    fruitCount = fruitFinder()
    answerSender(fruitCount)
    timesRan += 1

print(child.before)