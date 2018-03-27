from django.http import HttpResponse, HttpResponseRedirect



# def home(request):
# 	#print(request)
# 	#print(dir(request))
# 	print(request.method)
# 	print(request.is_ajax)
# 	print(request.is_ajax())
# 	return HttpResponse("<!DOCTYPE html><html> <head> <style> h1{color:red;} </style> </head> <body><h1>Hellow World</h1></body></html>")

def home(request):
	response = HttpResponse(content_type = 'application/json')
	response = HttpResponse(content_type = 'text/html')
	response.content = "<!DOCTYPE html><html> <head> <style> h1{color:red;} </style> </head> <body><h1>Hellow World</h1></body></html>"
	print(response.status_code)
	print(dir(response))
	#response.write("<p> Page not found. </p>")
	response.status_code = 404
	return response

def redirect_somewhere(request):
	return HttpResponseRedirect("/some/path")