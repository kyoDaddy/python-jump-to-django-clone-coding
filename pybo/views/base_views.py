from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from ..models import Question


def index(request):
    """
    초기 화면
    """
    # 페이지 : 입력인자
    page = request.GET.get('page', '1')
    # 검색어
    kw = request.GET.get('kw', '')
    # 정렬기준
    so = request.GET.get('so', 'recent')

    if so == 'recommend':
        # annotate 함수는 Question 모델의 기존 필드에 num_voter 필드를 임시로 추가해 주는 함수
        # 그러면 filter or order_by 에서 num_voter 를 사용할 수 있게 됨
        question_list = Question.objects.annotate(
            num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(
            num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:
        # 조회 : order_by(-붙으면 역순, 정렬할 속성)
        question_list = Question.objects.order_by('-create_date')

    if kw:
        # xx_icontains=(대소문자 가리지 않고 찾아줌)
        question_list = question_list.filter(
            Q(subject__icontains=kw) |                  # 제목 검색
            Q(content__icontains=kw) |                  # 내용 검색
            Q(author__username__icontains=kw) |         # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)   # 답변 글쓴이 검색
        ).distinct()

    # 페이징 처리 (10개씩 보여주기)
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}
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