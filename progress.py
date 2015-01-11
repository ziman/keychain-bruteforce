import time

def human(sec):
    result = ""

    if sec > 86400:
        result += "%dd" % (sec / 86400)
        sec %= 86400

    if sec > 3600:
        result += "%dh" % (sec / 3600)
        sec %= 3600

    if sec > 60:
        result += "%dm" % (sec / 60)
        sec %= 60

    if sec > 0:
        result += "%ds" % sec

    return result

class ProgressMeter(object):
    def __init__(self, totalItemCount):
        self.totalItemCount = totalItemCount
        self.startTime = time.time()
        self.secondsElapsed = 0.0
        self.itemsDone = 0
        
    def nextItem(self):
        self.secondsElapsed = int(time.time() - self.startTime)
        self.itemsDone += 1
        
    def __str__(self):
        es = self.secondsElapsed % 60
        em = self.secondsElapsed / 60
        
        if self.itemsDone:
            eta = self.secondsElapsed * (self.totalItemCount - self.itemsDone) / self.itemsDone
        else:
            eta = 0
        
        pp = 100*self.itemsDone / self.totalItemCount
        
        return "[%d/%d, %s, %d%%, ETA %s]" \
            % (self.itemsDone, self.totalItemCount, human(self.secondsElapsed), pp, human(eta))
