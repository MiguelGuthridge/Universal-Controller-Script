"""
eventprocessor > pluginprocessors > _template.py

Adapted from Novation LaunchKey Mk2 Script by Miguel Guthridge.
Available under GNU GPL3 at https://github.com/MiguelGuthridge/Novation-LaunchKey-Mk2-Script
Adapted from v2.0.0

The file acts as a template for plugin handlers. Copy it and edit to add your own plugin handlers.
To get it to be imported by the event processor, add its filename (without the .py) to processplugins.py

Author: Miguel Guthridge
"""

# Add names of plugins your script can process to this list
PLUGINS = ["Example Plugin"]


# Import any modules you might need
import config
import internal
import eventconsts


def topPluginStart():
    """Called when plugin is top plugin (not neccesarily focused)
    """
    return

def topPluginEnd():
    """Called when plugin is no longer top plugin (not neccesarily focused)
    """
    return

def activeStart():
    """Called when plugin brought to foreground (focused)
    """
    
    return

def activeEnd():
    """Called when plugin no longer in foreground (end of focused)
    """
    
    return

def process(command):
    """Called when processing commands. 

    Args:
        command (ParsedEvent): contains useful information about the event. 
            Use this to determing what actions your processor will take.
    """
    
    # Add event processor to actions list (useful for debugging)
    command.addProcessor("Your Processor Name")

    # When you handle your events, use command.handle("Some action") to handle events.

    return


