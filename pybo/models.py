from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    # User 모델을 ForeignKey로 적용하여 선언
    # on_delete=models.CSCADE (계정이 삭제되면 계정과 연결된 Question 모델 데이터를 모두 삭제하라는 의미)
    # related_name='' (특정 사용자가 작성한 질문을 얻기 위해서는 som_user.author_question.all() 처럼 사용할 수 있다.)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                               related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    # null=True 시 어떤 조건으로든 값을 비워둘 수 있음 form.is_valid 검사시 값이 없어도 됨
    modify_date = models.DateTimeField(null=True, blank=True)
    # 하나의 질문에 여러명이 추천가능, 한명이 여러 개의 질문에 추천 가능하므로 N:N 관계임 (manyToMany)
    voter = models.ManyToManyField(User, related_name='vote_question')

    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    # 질문 or 답변에 댓글 가능하므로 null 허용
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)


