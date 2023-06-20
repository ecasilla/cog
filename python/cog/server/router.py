import importlib
from typing import Any, Optional, Type, Dict

def perform_dynamic_import(module_name: str, attribute_name: str) -> Optional[Type[Any]]:
    try:
        # Import the module dynamically
        module = importlib.import_module(module_name)
        
        # Access the desired attribute dynamically
        attribute = getattr(module, attribute_name)
        
        return attribute
        
    except ImportError:
        # Handle import errors
        print(f"Failed to import module '{module_name}'")
        return None
    
    except AttributeError:
        # Handle attribute errors
        print(f"Attribute '{attribute_name}' not found in module '{module_name}'")
        return None

def find_router(config: Dict[str, Any]):
    if config["router"] is not None:
        perform_dynamic_import(config["router"]["module"], config["router"]["routes"])
