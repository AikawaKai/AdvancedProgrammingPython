import importrerun
import importlib

print(importrerun.spam)
importrerun.spam = "prova"
print(importrerun.spam)
import importrerun
print(importrerun.spam)
importlib.reload(importrerun)
print(importrerun.spam)
