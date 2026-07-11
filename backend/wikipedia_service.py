import wikipedia


def get_fact(topic):
    try:
        results = wikipedia.search(topic)

        if not results:
            return "No information found."

        page = results[0]

        summary = wikipedia.summary(page, sentences=2)

        return summary

    except wikipedia.DisambiguationError as e:
        try:
            summary = wikipedia.summary(e.options[0], sentences=2)
            return summary
        except Exception:
            return "No information found."

    except Exception:
        return "No information found."