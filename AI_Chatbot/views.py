from django.shortcuts import render,redirect
from google import genai
from django.conf import settings
from .models import ConversationModel,MessageModel
from .forms import ChatForm
from google.genai import types
# Create your views here.
client=genai.Client(api_key=settings.GEMINI_API_KEY)
def ChatView(request):
    session_key=request.session.session_key
    if not request.session.session_key:
        request.session.create()
        session_key=request.session.session_key
    conversation , created =ConversationModel.objects.get_or_create(session_id=session_key)


   
    reply=None
    if  request.method == 'POST':
        form=ChatForm(request.POST)
        if form.is_valid():
           
            prompt=form.cleaned_data['user_message']
            MessageModel.objects.create(
                converstion=conversation,
                role='user',
                message=prompt,
                
            )
            
            all_messages=MessageModel.objects.filter(converstion=conversation).order_by('timestamp')
            history=[]
            for msg in all_messages[::-1]:
                if msg.role == 'user':
                    history.append(types.Content(
                        role='user',
                        parts=[types.Part.from_text(text=msg.message)]
                    ) )
                else :
                    history.append( types.Content(
                        role='model',parts=[types.Part.from_text(text=msg.message)]
                    ) )   
                    system_prompt = (
            "You are a helpful AI assistant. "
            "Do not repeat your identity as an AI or mention you are not an SDE unless explicitly asked. "
            "Focus only on the user's latest question and provide concise, interesting facts."
        ) 
            full_prompt = f"{system_prompt}\n\nUser Question: {prompt}"
            try:
                chat=client.chats.create(model='gemini-2.5-flash',history=history)
                response=chat.send_message(full_prompt)
                ai_reply=response.text
                MessageModel.objects.create(converstion=conversation,role='model',message=ai_reply)
            except Exception as e:
                print(e)
    else :
        form=ChatForm()
    messages=MessageModel.objects.filter(converstion=conversation).order_by('timestamp')
    return render(request,'AI_Chatbot/form.html',{
            'form':form,
            'message':messages,
            'conversation':conversation

        })
def clear_chat(request):
    session_key=request.session.session_key
    if session_key :
        ConversationModel.objects.filter(session_id=session_key).delete()
    return redirect('chat-view')