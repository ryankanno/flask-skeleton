import importlib
import inspect


def load_module_instances(module_name):
    mod = importlib.import_module(module_name)
    return [ext for ext in mod.__dict__.itervalues() if 
        hasattr(ext, '__dict__') and not inspect.isclass(ext)]
