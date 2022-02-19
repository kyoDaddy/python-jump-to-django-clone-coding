import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


# 마크다운 필터 등록하기
@register.filter()
def mark(value):
    # 확장 도구 설정
    # nl2br (줄발꿈 문자를 <br> 태그로 치환), fenced_code (소스코드 표현 적용)
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))


# 템플릿에서 해당 함수를 필터로 사용할 수 있게 됨
@register.filter
def sub(value, arg):
    return value - arg
