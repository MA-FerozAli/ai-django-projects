from django.shortcuts import render
from django.conf import settings
from google import genai
from .form import DictionaryForm




def dictionary_view(request):
    result = None
    word_searched = None
    error = None

    if request.method == "POST":
        form = DictionaryForm(request.POST)

        if form.is_valid():
            word = form.cleaned_data["word"].strip()
            word_searched = word

            prompt = f"""
You are a professional dictionary assistant.
For the word "{word}", provide the following information.

Return ONLY a JSON object — no markdown, no backticks, no explanation.

{{
  "word": "{word}",
  "part_of_speech": "noun / verb / adjective / etc.",
  "phonetic": "/fəˈnɛtɪk/",
  "definition": "Clear, concise definition here.",
  "synonyms": ["word1", "word2", "word3", "word4", "word5"],
  "antonyms": ["word1", "word2", "word3"],
  "examples": [
    "First example sentence using {word}.",
    "Second example sentence using {word}.",
    "Third example sentence using {word}."
  ],
  "origin": "Brief etymology or origin of the word."
}}
"""

            try:
                client = genai.Client(api_key=settings.GEMINI_API_KEY)
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt,
                )
                raw = response.text.strip()

                # Strip markdown code fences if Gemini wraps in ```json
                if raw.startswith("```"):
                    raw = raw.split("```")[1]
                    if raw.startswith("json"):
                        raw = raw[4:]

                import json
                result = json.loads(raw.strip())

            except Exception as e:
                error = f"Could not fetch definition: {str(e)}"
    else:
        form = DictionaryForm()

    return render(request, "dictionary/index.html", {
        "form": form,
        "result": result,
        "word_searched": word_searched,
        "error": error,
    })