from django.shortcuts import render
from google import genai  # Correct import for the new SDK
from .forms import SummarizeForm
from django.conf import settings
def summarize_view(request):
    api_key =settings.GEMINI_API_KEY
    summary = None
    error=None
    
    if request.method == "POST":
        form = SummarizeForm(request.POST)

        if form.is_valid():
            user_text = form.cleaned_data['text']  
            try :  
                client = genai.Client(api_key=api_key)
                prompt = f"Summarize the following text in 3-5 concise sentences:\n\n{user_text}"
                # Temporary debug line
               
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )
              
                summary = response.text
               
            except Exception as e:
                
                error = f"API ERROR:{str(e)}"
                print(f"DEBUG: Error occurred: {e}") # Check your terminal for this!
    else:
        form = SummarizeForm()
        
    return render(request, 'summarizer/index.html', {
        'form': form,
        'summary': summary,
        "error":error,
    })