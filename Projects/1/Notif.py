# Events registered for mouse button
# down events
MOUSEBUTTONDOWN_EVENTS = []

# Register mouse button down event
def registerMBDEvent(callback):
    MOUSEBUTTONDOWN_EVENTS.append(callback)

# Notify subscribers of mouse
# button down event
def notifyMBDEvent(x, y):
    for callback in MOUSEBUTTONDOWN_EVENTS:
        callback(x, y)