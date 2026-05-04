from django.shortcuts import render
from google import genai
from .form import SEOForm
from django.conf import settings
# Create your views here.

def seo_prompt(blog_title,keywords):
    prompt=f" You are expert SEO copywriter Blog Post Title :{blog_title}  Target Keywords :{keywords} Generate the following using Exactly these labels: META_DESCRIPTION: [write one compelling meta description 150-160 charters max] META_TAGS: [list exactly 6 seo tags ,comma-seprated ,nohashtags]"
    return prompt

def parse_genai_response(response):
    meta_description=""
    meta_tags=""
    if "META_DESCRIPTION:" in response and "META_TAGS:" in response:
        parts = response.split("META_TAGS:")
        meta_description = parts[0].replace("META_DESCRIPTION:", "").strip()
        meta_tags=parts[1].strip()
    return meta_description ,meta_tags

def seo_generator(request):
    form=SEOForm()
    Meta_Description=None
    Meta_Tags=None
    if request.method == 'POST':
        form=SEOForm(request.POST)

        if form.is_valid():
            blog_title=form.cleaned_data['blog_title']
            keywords=form.cleaned_data['keywords']
            
         
            try:
                client=genai.Client(api_key=settings.GEMINI_API_KEY)
                prompt=seo_prompt(blog_title,keywords)
                response=client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt
                )
                print(f"GenAI Response: {response.text}")
                Meta_Description , Meta_Tags =  parse_genai_response(response.text)
            except Exception as e:
                print(f"Error: {(e)}")
    else:
        form=SEOForm()
    return render(request,'SEO_Metadata_generator/seo.html',{
        'form':form,
        'meta_description':Meta_Description,
        'meta_tags':Meta_Tags
    })
    

