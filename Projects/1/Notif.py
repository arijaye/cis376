MOUSEBUTTONDOWN_EVENTS = [] # make into a list?

def registerMBDEvent(callback):
    MOUSEBUTTONDOWN_EVENTS.append(callback)

    
def notifyMBDEvent(event, x, y):
    for callback in MOUSEBUTTONDOWN_EVENTS:
        callback(event, x, y)