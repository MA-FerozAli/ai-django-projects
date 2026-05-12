from django.shortcuts import render
from google import genai
from django.conf import settings
from .models import Code_History
from .forms import CodeForm

# Create your views here.

def code_explainer(request):
    form=CodeForm()
    result=None
    history=Code_History.objects.all().order_by('-created_at')[:5]
    if request.method =="POST":
        form=CodeForm(request.POST)
   
        if form.is_valid():
            users_code=form.cleaned_data['user_code']
            
            prompt = f"""
Act as a Senior Software Engineer and expert code mentor.
here is a code snippet:{users_code}
When explaining code, STRICTLY follow this format:

## 1. 🎯 Summary

Give a 1–2 sentence high-level overview of the code’s purpose.

## 2. 🛠️ Step-by-Step Breakdown

* Explain the code flow in logical order.
* Use **bold** for functions, classes, and variables.
* Explain both:

  * what the code does
  * why it is implemented that way
* Mention important logic, data flow, conditions, API/database interactions, and engineering decisions.

## 3. 💡 Key Concept

Identify the main programming concept used and explain:

* what it is
* why it matters
* how this code applies it

## 4. 🚀 Improvement Tip

Suggest one professional improvement related to:

* performance
* readability
* maintainability
* security
* scalability
* or error handling

Use clean Markdown formatting and keep explanations clear, concise, and beginner-friendly while maintaining professional engineering depth.

"""
        
            if request.session.get('last_code') == users_code:
                result=request.session.get('last_explaination')

            try:
                client=genai.Client(api_key=settings.GEMINI_API_KEY)
                response=client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt
                    
                )
                result=response.text
                Code_History.objects.create(code_snippet=users_code,code_explanation=result)
                request.session['last_code']=users_code
                request.session['last_explaination']=result
            except Exception as e:
                print(f"Error :{str(e)}")
    return render(request,'code_explainer/index.html',{
        'form':form,
        'result':result,
        'history':history
    })