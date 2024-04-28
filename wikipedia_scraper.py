import wikipedia

def get_wikipedia_summary(topic, sentences=5):
    try:
        wikipedia.set_lang("en")
        summary = wikipedia.summary(topic, sentences=sentences)
        return summary
    except wikipedia.exceptions.PageError:
        return f"No Wikipedia page found for '{topic}'."
    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options[:5]
        return f"Disambiguation page found for '{topic}'. Options: {', '.join(options)}."
