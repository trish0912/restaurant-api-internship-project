
from django.shortcuts import render, redirect
from .forms import ContactForm

from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to DB or send email
            form.save()  # optional
            return render(request, 'contact/contact.html', {
                'form': ContactForm(),  # empty form after success
                'success': True
            })
    else:
        form = ContactForm()

    # For GET requests or invalid POST, return form with errors
    return render(request, 'contact/contact.html', {'form': form})

    

def about_view(request):
    return render(request, 'contact/about.html')