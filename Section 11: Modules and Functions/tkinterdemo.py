try:
    import tkinter
except ImportError: # on python 2
    import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

tkinter._test()