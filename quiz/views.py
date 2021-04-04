from django.shortcuts import render
from quiz.models import Quiz

def qpage(request):
	questions = Quiz.objects.all()
	for q in questions:
		if q.ques_image:
			print(q.ques_image.url)
	return render(request, 'quiz.html', { 'questions': questions})
	
	
