from django.shortcuts import render,redirect,get_object_or_404
from .models import Facts
from .forms import CompanyFactForm,QuestionForm
from google import genai
from django.conf import settings


# Create your views here.

def fact_list(request):
    facts=Facts.objects.all()
    return render(request,'smart_FAQ_manager/list.html',{'facts':facts})

def fact_create(request):
    form=CompanyFactForm()
    result=None
    if request.method=="POST":
        form=CompanyFactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list')
    else:
        form=CompanyFactForm()
    return render(request,'smart_FAQ_manager/fact.html',{
         'form':form
       
    })
def fact_update(request,pk):
    obj=get_object_or_404(Facts,pk=pk)
    form=CompanyFactForm(request.POST or None,instance=obj)
    if request.method == 'POST' and  form.is_valid() :
        form.save()
        return redirect('list')
    return render(request,'smart_FAQ_manager/fact.html',{
         'form':form
       
    })
def fact_delete(request,pk):
    obj=get_object_or_404(Facts,pk=pk)
    obj.delete()
    return redirect('list')

def ask_question(request):
    form=QuestionForm()
    answer=None
    if request.method =="POST":
        form=QuestionForm(request.POST)
        if form.is_valid():
            fact_queryset=Facts.objects.all()
            context='\n'.join([f"Title : {f.title}\nContent: {f.content}\n---" for f in fact_queryset ])
            question=form.cleaned_data['question']
            prompt=f""" You are a company FAQ Assistant .
            Answer the user's question ONLY using the facts below .
            If the answer is not in the facts ,,say : "I don't have information on that."

            COMPANY FACTS :
            {context}

            USER QUESTION:
            {question}
            """
            try :
                client=genai.Client(api_key=settings.GEMINI_API_KEY)
                response=client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt
                )
                answer=response.text
            except Exception as e :
                print(f'error:{str(e)}')
    else:
        form=QuestionForm()
    return render(request,'smart_FAQ_manager/form.html',{
        'form':form,
        'answer':answer
    })