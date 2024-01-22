"""
LetMeDoIt AI Plugin - search latest news

search latest news

[FUNCTION_CALL]
"""

from letmedoit import config
import feedparser

# Function method to get the latest news from a specific RSS feed
def search_latest_news(function_args: dict) -> str:
    keywords = function_args.get("keywords")
    feed_url = f"https://news.google.com/rss/search?q={keywords}&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(feed_url)

    # Print the title and link of each news item
    config.stopSpinning()
    config.print2(config.divider)
    for index, entry in enumerate(feed.entries):
        if index < 10:
            if not index == 0:
                config.print2(config.divider)
            config.print(entry.title)
            print(entry.link)
    config.print2(config.divider)
    return ""

# Function signature to work with ChatGPT function calling
functionSignature = {
    "name": "search_latest_news",
    "description": "Search the latest news with given keywords",
    "parameters": {
        "type": "object",
        "properties": {
            "keywords": {
                "type": "string",
                "description": "The keywords for searching the latest news, delimited by plus sign '+'.  For example, return 'London+UK' if keywords are 'London' and 'UK'.",
            },
        },
        "required": ["keywords"],
    },
}

# Add the following line to tell LetMeDoIt AI that this plugin work with function calling feature.
config.pluginsWithFunctionCall.append("search_latest_news")

# The following line adds the function signature, that we prepared in STEP 3, to the full list of all function signatures that work with LetMeDoIt AI.
config.chatGPTApiFunctionSignatures.append(functionSignature)

# The following line tells LetMeDoIt AI to call the method "search_latest_news" that we added in this plugin when the function signature "search_latest_news" is loaded.
config.chatGPTApiAvailableFunctions["search_latest_news"] = search_latest_news

# The following line is optional. It adds an input suggestion to LetMeDoIt AI user input prompt
config.inputSuggestions.append("Tell me the latest news about ")