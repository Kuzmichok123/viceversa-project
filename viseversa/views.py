from django.shortcuts import render


def home(request):
	return render(request, 'home.html')


def reverse(request):
	user_text = request.GET['usertext']
	text_reverse = user_text[::-1]
	count = []
	count += user_text.split()
	count = len(count)
	return render(request, 'reverse.html', {'user_text': user_text, 'text_reverse':text_reverse, 'count': count})
