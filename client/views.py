from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate , logout
from django.contrib import messages
from .models import AddpostModel
from .models import add_question

def AddPost(request):
    if request.user.is_authenticated and request.user.role == "Client":
        print(request.user.role)
        current_user = request.user
        if current_user.role == "Client":
             if request.method == 'POST':
                post_title = request.POST.get("post_title")
                post_content = request.POST.get("post_content")
                tags = request.POST.get("tags")
                bidamount = request.POST.get("bidamount")
                user_role = request.POST.get("user_role")
                user_id = request.POST.get("user_id")
                data = {
                    'post_title': post_title,
                    'post_content': post_content,
                    'user_role' : user_role,
                    'tags' : tags,
                    'bidamount' : bidamount,
                    'user_id' : user_id,
                }
                addpost = AddpostModel(post_title=post_title, post_content=post_content, user_role=user_role, user_id=request.user.id , tags=tags , bidamount=bidamount)
                addpost.save()
                print(data)
                messages.success(request, "Post Added")
        return render(request, 'clientpost.html' , {'current_user': current_user})
    else:
       return redirect('index')

def AddQuestion(request):
    if request.user.is_authenticated and request.user.role == "User":
        print(request.user.role)
        current_user = request.user
        if current_user.role == "User":
             if request.method == 'POST':
                question = request.POST.get("question")
                question_des = request.POST.get("question_des")
                tags = request.POST.get("tags")
                user_role = request.POST.get("user_role")
                user_id = request.POST.get("user_id")
                username = request.POST.get("username")
                votecount = 0
                dislike = 0
                data = {
                    'question': question,
                    'question_des': question_des,
                    'user_role' : user_role,
                    'tags' : tags,
                    'user_id' : user_id,
                    'votecount' : votecount,
                    'dislike' : dislike,
                    'username' : username,
                }
                print(data)
                addquestion = add_question(question=question, question_des=question_des, user_role=user_role, user_id=request.user.id , tags=tags , votecount=votecount, dislike=dislike , username=username )
                addquestion.save()
                print(data)
                messages.success(request, "Question Added")
        return render(request, 'addquestion.html' , {'current_user': current_user})
    else:
       return redirect('index')

def allpost(request):
     if request.user.is_authenticated and request.user.role == "Client":
       Allposts=AddpostModel.objects.filter(user_id=request.user.id).values()
       return render(request, 'viewpost.html' , {'Allposts' : Allposts})

def allque(request):
     if request.user.is_authenticated and request.user.role == "User":
       viewAllquestions = add_question.objects.filter(user_id=request.user.id).values()
       return render(request, 'viewquestion.html' , {'viewAllquestions' : viewAllquestions})
     else:
       return redirect('index')

def update(request,id):
    if request.user.is_authenticated and request.user.role == "User":
       viewAllquestions = add_question.objects.get(id=id)
       if request.method=="POST":
          viewAllquestions.question = request.POST.get("question")
          viewAllquestions.question_des = request.POST.get("question_des")
          viewAllquestions.tags      = request.POST.get("tags")
          viewAllquestions.save()
          messages.success(request, "Data Updated")


       return render(request, 'update.html' , {'viewAllquestions' : viewAllquestions})
        
def delete(request,id):
     if request.user.is_authenticated:
        deleteData = add_question.objects.get(id=id)
        deleteData.delete()
        messages.error(request, "Delete")
        return redirect("/delete")
     return render(request, 'viewquestion.html')
