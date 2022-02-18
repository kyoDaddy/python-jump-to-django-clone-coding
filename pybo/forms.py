from django import forms
from pybo.models import Question, Answer, Comment


# 장고 폼 (forms.Form, forms.ModelForm)
# 장고 모델 폼은 내부 클래스로 Meta 클래스를 반드시 가져야 함, Meta 클래스에는 모델 폼이 사용할 모델과 모델의 필드들이 있어야 함
class QuestionForm(forms.ModelForm):
    # QuestionForm <-> Question 모델과 연결되어 있으며, 필드로 subject, content를 사용한다고 정의함
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }
        # {{ form.as_p }} 완벽하지는 않지만 부트스트랩 적용을 위한 widgets 필드 사용
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class':'form-control'}),
        #     'content': forms.Textarea(attrs={'class':'form-control', 'rows': 10})
        # }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용'
        }