from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    # 멤버 변수 = models.외래키(참조하는 객체) 
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # 역참조 값 설정 related_name = , omments
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f'Article:{self.article}, {self.pk}-{self.content}'

#python manage.py shell_plus