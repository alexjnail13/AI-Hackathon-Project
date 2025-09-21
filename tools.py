def save_tool(content, filename):
	"""
	Save the given content to a file.
	Args:
		content (str): The content to save.
		filename (str): The name of the file to save to.
	Returns:
		str: Success message or error message.
	"""
	try:
		with open(filename, 'w', encoding='utf-8') as f:
			f.write(content)
		return f"Content saved to {filename}"
	except Exception as ex:
		return f"Error saving file: {ex}"
# from wikipedia import summary

def wiki_tool(query, sentences=2):
	"""
	Search Wikipedia for the given query and return a summary.
	Args:
		query (str): The search query.
		sentences (int): Number of sentences in the summary.
	Returns:
		str: Summary of the Wikipedia page.
	"""
	import wikipedia
	try:
		return wikipedia.summary(query, sentences=sentences)
	except wikipedia.exceptions.DisambiguationError as e:
		return f"Disambiguation error: {e.options}"
	except wikipedia.exceptions.PageError:
		return "Page not found."
	except Exception as ex:
		return f"Error: {ex}"
# from duckduckgo_search import DDGS

def search_tool(query, max_results=5):
	"""
	Search DuckDuckGo for the given query and return results.
	Args:
		query (str): The search query.
		max_results (int): Maximum number of results to return.
	Returns:
		list: List of result dictionaries with 'title', 'link', and 'snippet'.
	"""
	from duckduckgo_search import DDGS
	results = []
	with DDGS() as ddgs:
		for r in ddgs.text(query, max_results=max_results):
			results.append({
				'title': r.get('title'),
				'link': r.get('href'),
				'snippet': r.get('body')
			})
	return results
