from django.http import HttpResponse
import funcoes


def view_1(request):
    funcoes.add_visita('1')
    return HttpResponse("""
<h1>
301 Redirect <br>
Location:http://google.com
<meta http-equiv="refresh" content="0; URL='http://google.com'"/>
</h1>
    """)
    
def view_2(request):
    funcoes.add_visita('2')
    return HttpResponse("""
<h1>
301 Redirect <br>
Location:http://google.com
<meta http-equiv="refresh" content="0; URL='http://google.com'"/>
</h1>
    """)
    
def view_3(request):
    funcoes.add_visita('3')
    return HttpResponse("""
<h1>
301 Redirect <br>
Location:http://google.com
<meta http-equiv="refresh" content="0; URL='http://google.com'"/>
</h1>
    """)
    
def view_4(request):
    funcoes.add_visita('4')
    return HttpResponse("""
<h1>
301 Redirect <br>
Location:http://google.com
<meta http-equiv="refresh" content="0; URL='http://google.com'"/>
</h1>
    """)
    
def view_5(request):
    funcoes.add_visita('5')
    return HttpResponse("""
<h1>
301 Redirect <br>
Location:http://google.com
<meta http-equiv="refresh" content="0; URL='http://google.com'"/>
</h1>
    """)
    
def view_6(request):
    funcoes.add_visita('6')
    return HttpResponse("""
<h1>
301 Redirect <br>
Location:http://google.com
<meta http-equiv="refresh" content="0; URL='http://google.com'"/>
</h1>
    """)
    
def view_7(request):
    funcoes.add_visita('7')
    return HttpResponse("""
<h1>
301 Redirect <br>
Location:http://google.com
<meta http-equiv="refresh" content="0; URL='http://google.com'"/>
</h1>
    """)
    
def view_8(request):
    funcoes.add_visita('8')
    return HttpResponse("""
<h1>
301 Redirect <br>
Location:http://google.com
<meta http-equiv="refresh" content="0; URL='http://google.com'"/>
</h1>
    """)
    
def view_9(request):
    funcoes.add_visita('9')
    return HttpResponse("""
<h1>
301 Redirect <br>
Location:http://google.com
<meta http-equiv="refresh" content="0; URL='http://google.com'"/>
</h1>
    """)
    
def view_a(request):
    funcoes.add_visita('a')
    return HttpResponse("""
<h1>
301 Redirect <br>
Location:http://google.com
<meta http-equiv="refresh" content="0; URL='http://google.com'"/>
</h1>
    """)
    
def view_b(request):
    funcoes.add_visita('b')
    return HttpResponse("""
<h1>
301 Redirect <br>
Location:http://google.com
<meta http-equiv="refresh" content="0; URL='http://google.com'"/>
</h1>
    """)
    