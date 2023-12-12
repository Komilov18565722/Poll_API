from django.urls import path
from .views import polls_list, polls_detail

from .apiviews import PollList, PollDetail, ChoiceList, CreateVote, UserCreate, LoginView

# from rest_framework_swagger.views import get_swagger_view

from rest_framework.routers import DefaultRouter
from .apiviews import PollViewSet


# schema_view = get_swagger_view(title='Polls API')

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

urlpatterns = [
	# path('polls/', PollList.as_view(), name = 'polls_list'),
	path('users/', UserCreate.as_view(), name = 'create_user'),
	path('login/', LoginView.as_view(), name = 'login'),
	path('polls/<int:pk>/choices/', ChoiceList.as_view(), name = 'choices_list'),
	path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name = 'create_vote'),
	# path(r'swagger-docs/', schema_view),
]




urlpatterns += router.urls