from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    # User 모델을 ForeignKey로 적용하여 선언
    # on_delete=models.CSCADE (계정이 삭제되면 계정과 연결된 Question 모델 데이터를 모두 삭제하라는 의미)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    # null=True 시 어떤 조건으로든 값을 비워둘 수 있음 form.is_valid 검사시 값이 없어도 됨
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    # 질문 or 답변에 댓글 가능하므로 null 허용
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)


