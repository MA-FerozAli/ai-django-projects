from django.shortcuts import render
from .forms import JokeQuoteForm
from google import genai
from django.conf import settings
# Create your views here.

def joke_view(request):
    form=JokeQuoteForm()
    quote=None
    if request.method == 'POST':
        form=JokeQuoteForm(request.POST)
        if form.is_valid():
            content_type=form.cleaned_data['content_type']
            persona=form.cleaned_data['persona']
            prompt = f"Your are a {persona},Tell me a{content_type}"

            try :
                client =genai.Client(api_key=settings.GEMINI_API_KEY)
                response=client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt
                )
                quote=response.text
                print(quote)
            except Exception as e:
                print(f"Error:{(e)}")
    else:
        form =JokeQuoteForm()
    return render(
        request,"jokeGenerator/index.html",{'form':form,
        'quote':quote}
    )