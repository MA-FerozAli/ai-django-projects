from django import forms

CONTENT_CHOICES=[
    ('','---Select Content Type ---'),
    ('joke','Tell me a joke'),
    ('quote','Tell me a quote'),
]
PERSONA_CHOICE=[
    ('','---Choose a Persona---'),
    ('a sarcastic robot','Sarcastic Robot'),
    ('a funny pirate','Pirate'),
    ('a wise philosopher','Philosopher'),
    ('a motivational coach','Coach'),
]
class JokeQuoteForm(forms.Form):
    content_type=forms.ChoiceField(choices=CONTENT_CHOICES,
    label="what should i generate?")
    persona=forms.ChoiceField(choices=PERSONA_CHOICE,
    label="select the AI's Personality")