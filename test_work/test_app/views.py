import json
import requests
from django.shortcuts import render
from .models import Posts, Users, Adress, Company
from django.core import exceptions


# Create your views here.
def index(request):
    #Запрос данных
    users = json.loads(requests.get('http://jsonplaceholder.typicode.com/users').content)
    posts = json.loads(requests.get('http://jsonplaceholder.typicode.com/posts').content)
    
    #Заполняем базу данными юзеров
    for user in users:
        try:
            user_temp = Users.objects.get(user_id=user['id'])
        except exceptions.ObjectDoesNotExist:
            user_data = Users(user_id=user['id'],
                                name=user['name'],
                                username=user['username'],
                                email=user['email'],
                                phone=user['phone'],
                                website=user['website'],
                                )
            user_data.save()

            adress_data = Adress(user_id=Users(user_id=user['id']),
                                city=user['address']['city'],
                                street=user['address']['street'],
                                suite=user['address']['suite'],
                                zipcode=user['address']['zipcode'],
                                lat = user['address']['geo']['lat'],
                                lng = user['address']['geo']['lng'],
                                )
            adress_data.save()

            company_data = Company(user_id=Users(user['id']),
                                    name=user['company']['name'],
                                    catchPhrase=user['company']['catchPhrase'],
                                    bs=user['company']['bs'],
                                    )
            company_data.save()
            
    #Заполняем базу данными постов
    for post in posts:
        try:
            post_temp = Posts.objects.get(post_id=post['id'])
        except exceptions.ObjectDoesNotExist: 
            user = Users.objects.get(user_id=post['userId'])
            posts_data = Posts(user_id=Users(post['userId']),
                                post_id=post['id'],
                                title=post['title'],
                                body=post['body'],
                                username=user.username,
                                )
            posts_data.save()

    #Вывод данных на страницу
    all_posts = []
    for post in Posts.objects.all():
        data = {
            'name': post.username,
            'title': post.title,
            'body':post.body,
        }
        all_posts.append(data)
    
    context = {'info':all_posts}
    return(render(request, 'index.html', context))