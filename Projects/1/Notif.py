MOUSEBUTTONDOWN_EVENTS = [] # make into a list?

def registerMBDEvent(callback):
    MOUSEBUTTONDOWN_EVENTS.append(callback)

    
def notifyMBDEvent(x, y):
    for callback in MOUSEBUTTONDOWN_EVENTS:
        callback(x, y)