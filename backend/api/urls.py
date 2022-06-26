from django.urls import path,include
#from rest_framework.authtoken.views import obtain_auth_token # djoser
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *


urlpatterns = [
	# Auth
	path('auth/',include('djoser.urls')),
	path('auth/', include('djoser.urls.authtoken')),
	path('token/',TokenObtainPairView.as_view(),name='token_obtain_pair_view'),
	path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh_view'),
	# Executors enpoints
	path('executors/<int:pk>', ExecutorRetrieveView.as_view()),
	path('executors/update/<int:pk>', ExecutorUpdateView.as_view()),
	path('executors/all', ExecutorListView.as_view()),
	path('executors/new', CreateExecutorView.as_view()),
	# Customers enpoints
	path('customers/<int:pk>', CustomerRetrieveView.as_view()),
	path('customers/update/<int:pk>', CustomerUpdateView.as_view()),
	path('customers/all', CustomerListView.as_view()),
	path('customers/new', CreateCustomerView.as_view()),
	# Service enpoints
	path('services/<int:pk>', ServiceRetrieveView.as_view()),
	path('services/update/<int:pk>', ServiceUpdateView.as_view()),
	path('services/all', ServiceListView.as_view()),
	path('services/new', CreateServiceView.as_view()),
	# Order enpoints
	path('orders/<int:pk>', OrderRetrieveView.as_view()),
	path('orders/update/<int:pk>', OrderUpdateView.as_view()),
	path('orders/all', OrderListView.as_view()),
	path('orders/new', CreateOrderView.as_view()),
	# Ordering enpoints
	path('orderings/<int:pk>', OrderingRetrieveView.as_view()),
	path('orderings/update/<int:pk>', OrderingUpdateView.as_view()),
	path('orderings/all', OrderingListView.as_view()),
	path('orderings/new', CreateOrderingView.as_view()),
	# Tag enpoints
	path('tags/<int:pk>', TagRetrieveView.as_view()),
	path('tags/update/<int:pk>', TagUpdateView.as_view()),
	path('tags/all', TagListView.as_view()),
	path('tags/new', CreateTagView.as_view()),
	# Message enpoints
	path('message/<int:pk>', MessageRetrieveView.as_view()),
	path('message/update/<int:pk>', MessageUpdateView.as_view()),
	path('message/all', MessageListView.as_view()),
	path('message/new', CreateMessageView.as_view()),
	# Ticket enpoints
	path('tickets/<int:pk>', TicketRetrieveView.as_view()),
	path('tickets/update/<int:pk>', TicketUpdateView.as_view()),
	path('tickets/all', TicketListView.as_view()),
	path('tickets/new', CreateTicketView.as_view()),
	# Review enpoints
	path('reviews/<int:pk>', ReviewRetrieveView.as_view()),
	path('reviews/update/<int:pk>', ReviewUpdateView.as_view()),
	path('reviews/all', ReviewListView.as_view()),
	path('reviews/new', CreateReviewView.as_view()),
	# Authoring enpoints
	path('authorings/<int:pk>',AuthoringRetrieveView.as_view()),
	path('authorings/update/<int:pk>', AuthoringUpdateView.as_view()),
	path('authorings/all', AuthoringListView.as_view()),
	path('authorings/new', CreateAuthoringView.as_view()),
	
]

