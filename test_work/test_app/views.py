import json
import requests
from django.shortcuts import render
from .models import Posts, Users, Adress, Company


# Create your views here.
def index(request):
    #Запрос данных
    users = json.loads(requests.get('http://jsonplaceholder.typicode.com/users').content)
    posts = json.loads(requests.get('http://jsonplaceholder.typicode.com/posts').content)
    
    #Проверка какие данные уже есть в БД
    users_all = []
    posts_all = []
    Users_db = Users.objects.all()
    Posts_db = Posts.objects.all()
    for usr in Users_db:
        users_all.append(usr.user_id)
    for pst in Posts_db:
        posts_all.append(pst.post_id)
        
    #Заполняем базу данными юзеров
    for user in users:
        if user['id'] not in users_all:
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
        if post['id'] not in posts_all:
            if post not in Posts_db:
                for usr in Users_db:
                    if usr.user_id == post['userId']:
                        name = usr.username
                        posts_data = Posts(user_id=Users(post['userId']),
                                            post_id=post['id'],
                                            title=post['title'],
                                            body=post['body'],
                                            username=name,
                                            )
                        posts_data.save()

    #Вывод данных на страницу
    all_posts = []
    for post in Posts_db:
        data = {
            'name': post.username,
            'title': post.title,
            'body':post.body,
        }
        all_posts.append(data)
    
    context = {'info':all_posts}
    return(render(request, 'index.html', context))