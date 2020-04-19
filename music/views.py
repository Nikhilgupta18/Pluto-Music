from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return render(request,'index.html')

def Upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        context={
            'url':url,
        }
    return render(request,'upload.html',context)