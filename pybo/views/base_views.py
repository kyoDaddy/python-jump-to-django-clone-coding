from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question


def index(request):
    """
    초기 화면
    """
    # 페이지 : 입력인자
    page = request.GET.get('page', '1')

    # 조회 : order_by(-붙으면 역순, 정렬할 속성)
    question_list = Question.objects.order_by('-create_date')

    # 페이징 처리 (10개씩 보여주기)
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    # render 함수는 context 데이터를 html 코드로 변환한다.
    return render(request, 'pybo/question_list.html', context)
    # return HttpResponse("안녕하세요. pybo에 오신것을 환영합니다.")


# url-mapping
def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    # get_object_or_404 함수는 모델의 기본키를 이용하여 모델 객체 한 건을 반환한다.
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)