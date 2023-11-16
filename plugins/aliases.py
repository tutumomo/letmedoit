"""
myHand.ai plugin - aliases

add aliases
"""

import config, sys, os

config.aliases["!autogen"] = f"!{sys.executable} {os.path.join(config.myHandAIFolder, 'autogen_assistant.py')}"
config.aliases["!retriever"] = f"!{sys.executable} {os.path.join(config.myHandAIFolder, 'autogen_retriever.py')}"
config.aliases["!etextedit"] = f"!{sys.executable} {os.path.join(config.myHandAIFolder, 'eTextEdit.py')}",

config.inputSuggestions += ["!autogen", "!retriever", "!etextedit"]

# Example to set an alias to open-interpreter
#config.aliases["!interpreter"] = f"!env OPENAI_API_KEY={config.openaiApiKey} ~/open-interpreter/venv/bin/interpreter"