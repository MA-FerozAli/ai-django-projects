from django.shortcuts import render
from .form import  GrammerForm
from google import genai
from django.conf import settings

# Create your views here.
def GrammerView(request):
    form=GrammerForm()
    query=None
    if request.method == 'POST':
        form=GrammerForm(request.POST)

        if form.is_valid():
            userText=form.cleaned_data['UserText']
            tone=form.cleaned_data['tone']
            prompt=f"fix the grammer and tone of text: {userText}  by using this {tone} tone"
            try:
                client=genai.Client(api_key=settings.GEMINI_API_KEY)
                response=client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt
                )
                query=response.text
                #print(query)
            except Exception as e:
                print(str({e}))
        else:
            form=GrammerForm()    
    return render(request,
        'grammerToneFixer/index.html',{
            'form':form,
            'query':query,
        }
    )