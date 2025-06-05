import os, glob

current_dir = os.path.dirname(__file__)
modules = glob.glob(os.path.join(current_dir, "*_views.py"))

for m in modules:
    module_name = os.path.basename(m)[:-3]
    exec(f"from .{module_name} import *")