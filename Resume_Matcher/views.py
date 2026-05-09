from django.shortcuts import render
from google import genai
from django.conf import settings
from .forms import ResumeForm
# Create your views here.


def build_prompt(resume,jobDescription):
    prompt=""" You are expert ATS (Application Tracker System) and career coach
    Analyse The resume and job description below
    Respond in this EXACT format:
    MATCH SCORE: [X]%
    MATCHING SKILLS:
    - [skill 1]
    - [skill 2]

    MISSING SKILLS:
    - [skill 1]
    - [skill 2]

    TOP 3 IMPROVEMENTS TIPS:
    1. [tip]
    2. [tip]
    3. [tip]

    RESUME:
    {resume}

    JOB_DESCRIPTION:
    {jobDescription}
    """
    return prompt
def call_gemini(prompt):
    result=None
    error=None
    try :
        client=genai.Client(api_key=settings.GEMINI_API_KEY)
        response=client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        result=response.text
    except Exception as e :
        error =f" Error :{str(e)}"
    return (result ,error)

def Resume_Matcher_View(request):
    form=ResumeForm()
    result=None
    error=None
    if request.method == "POST":
        form=ResumeForm(request.POST)

        if form.is_valid():
            resume=form.cleaned_data['resume_text']
            job_description=form.cleaned_data['job_description']

            prompt=build_prompt(resume,job_description)
            result , error =call_gemini(prompt)
    else :
        form=ResumeForm()
    
    return render(request,'Resume_Matcher/form.html',
                {
                    'form':form,
                    'result':result,
                    'error':error
                })