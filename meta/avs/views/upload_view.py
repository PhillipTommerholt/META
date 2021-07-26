from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage


@login_required(login_url='login_view')
def upload_view(request):
    if request.method == 'POST':
        if request.FILES:
            uploaded_file = request.FILES['document']
            fs = FileSystemStorage()
            fs.save(uploaded_file.name, uploaded_file)

    return render(request, 'avs/upload.html')
