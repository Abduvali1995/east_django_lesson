from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_view(requets):
    html = '''
        <h1> Assalamu alaykum bzining web sayitimizga hush kelibsiz </h1>
        <p>bugun juda qiziq narsa o`rganyapmiz</p>
        <a href="second_view"> <h2>Python</h2> </a>
         <a href="three_view"> <h2>Django</h2> </a>
         <a href="five_view"> <h2>Html</h2> </a>
    '''
    return HttpResponse(html)

def second_view(request):
    html = '''
        <h1> Bu ikkinchi sahifa python haqida ma`lumot beradi </h1>
        <p>  python high level programming language python was created by G.Rossum</p>
        <a href="../"><h2>Home</h2></a>
    '''
    return HttpResponse(html)

def three_view(request):
    html = '''
          <h1> Bu 3- sahifa Django haqida ma`lumot beradi </h1>
          <p>  Django high level python programming framework python was created by G.Rossum</p>
          <a href="../"><h2>Home</h2></a>
          <a href="four_view"><h2>C++</h2></a>
      '''
    return HttpResponse(html)

def four_view(request):
    html = '''
             <h1> Bu 4- sahifa C++ haqida ma`lumot beradi </h1>
             <p>  C++ high level  programming  python was created by G.Rossum</p>
             <a href="three_view"><h2>Home</h2></a>
         '''
    return HttpResponse(html)

def five_view(request):
    html = '''
               <h1> Bu 4- sahifa C++ haqida ma`lumot beradi </h1>
               <p>  C++ high level  programming  python was created by G.Rossum</p>
               <a href="../"><h2>Home</h2></a>
           '''
    return HttpResponse(html)