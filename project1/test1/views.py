from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    html = """
    <html>
      <body>
        <center>
     <a href="about">about</a>

    </center>

<center>
     <a href="contact">contact</a>

    </center>

<center>
     <a href="home">home</a>
    </center>

<font color="red">
    <center>
        <h1>welcome   </h1>
    </center>
</font>
      </body>
    </html>
    """
    return HttpResponse(html)


def contact(request):
    return render(request, 'test1/contact.html')


def about(request):
    return render(request, 'test1/about.html')
