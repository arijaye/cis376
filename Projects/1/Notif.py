MOUSEBUTTONDOWN_EVENTS = []
KEY_EVENTS = []

def registerMBDEvent(callback):
    MOUSEBUTTONDOWN_EVENTS.append(callback)

    
def notifyMBDEvent(x, y):
    for callback in MOUSEBUTTONDOWN_EVENTS:
        callback(x, y)

def registerKeyEvent(callback):
    KEY_EVENTS.append(callback)

    
def notifyKeyEvent(key):
    for callback in KEY_EVENTS:
        callback(key)        