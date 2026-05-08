from django.shortcuts import render ,redirect,get_object_or_404
from .models import Blog
from .forms import BlogForm
from google import genai
from django.conf import settings
# Create your views here.
def generate_outline(request):
    form=BlogForm()
    outline=None
    if request.method == 'POST':
        form=BlogForm(request.POST)
        if form.is_valid():
            topic=form.cleaned_data['Topic']
            prompt = f"""
                Write a VERY BRIEF outline for the topic: '{topic}'.

                STRICT RULES:
                - Maximum 3 lines total.
                - No introductory text or concluding remarks.
                - Use simple bullet points.
                - Focus only on the core message.

                Example of desired length:
                * Introduction to the topic.
                * Key benefits and challenges.
                * Final summary and conclusion.
                """
            try:
                client=genai.Client(api_key=settings.GEMINI_API_KEY)
                response=client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                )
                outline=response.text
                obj =Blog.objects.create(topic=topic,outline=outline)
                return redirect('outline-details',pk=obj.pk)
            except Exception as e :
                print(F"Error:{str(e)}")
    else:
        form =BlogForm()
    return render(request,'BlogArchitect/index.html',{'form':form})

def outline_details(request,pk):
    blog =get_object_or_404(Blog,pk=pk)
    return render(request,'BlogArchitect/outline_details.html',
    {
        'blog':blog,
        'pk':pk
    })
def write_full_post(request,pk):
    full_post=None
    if request.method=='POST':
        outline=Blog.objects.get(pk=pk)
        topic=Blog.objects.get(pk=pk)
        prompt=prompt = f"""
            You are a professional long-form blog writer. 
            Using the following topic and outline, write a complete, high-quality blog post.

            TOPIC: {topic}
            OUTLINE: {outline}

            REQUIREMENTS:
            - Write in a conversational yet authoritative 'Thought Leader' tone.
            - Use Markdown formatting (bolding, lists, and headers) for readability.
            - Include a compelling introduction and a strong 'Call to Action' conclusion.
            - Ensure the content is original, insightful, and at least 800 words.
            """
        try:
                client=genai.Client(api_key=settings.GEMINI_API_KEY)
                response=client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                )
                full_post=response.text
                Blog.objects.filter(pk=pk).update(full_blog=full_post)
                return redirect('blog_result',pk=pk)
        except Exception as e :
                print(F"Error:{str(e)}")
    return redirect('outline-details',pk=pk)

def blog_result(request,pk):
    blog=get_object_or_404(Blog,pk=pk)
    return render(request,'BlogArchitect/full_blog.html',{
        'blog':blog,
    })