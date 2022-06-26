from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
		class Meta:
				model = User
				fields = ('id', 'username', 'email', 'first_name', 'last_name')
			
class ExecutorSerializer(serializers.ModelSerializer):
		user = UserSerializer(read_only=True)
		class Meta:
				model = Executor
				fields = '__all__'


class CreateExecutorSerializer(serializers.ModelSerializer):
		user = UserSerializer(required=True)
		class Meta:
				model = Executor
				fields = '__all__'

	
class CustomerSerializer(serializers.ModelSerializer):
		user = UserSerializer(read_only=True)
		class Meta:
				model = Customer
				fields = '__all__'


class CreateCustomerSerializer(serializers.ModelSerializer):
		user = UserSerializer(required=True)
		class Meta:
				model = Customer
				fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
		executor = ExecutorSerializer(read_only=True)
		service_type = serializers.CharField(source='get_service_type_display')
		class Meta:
				model = Service
				fields = '__all__'


class CreateServiceSerializer(serializers.ModelSerializer):
		executor = ExecutorSerializer(required=True)
		class Meta:
				model = Service
				fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
		customer = CustomerSerializer(read_only=True)
		order_type = serializers.CharField(source='get_order_type_display')
		class Meta:
				model = Order
				fields = '__all__'


class CreateOrderSerializer(serializers.ModelSerializer):
		customer = CustomerSerializer(required=True)
		class Meta:
				model = Order
				fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
		order = OrderSerializer(read_only=True)
		service = ServiceSerializer(read_only=True)
		class Meta:
				model = Tag
				fields = '__all__'


class CreateTagSerializer(serializers.ModelSerializer):
		order = OrderSerializer(required=True)
		service = ServiceSerializer(required=True)
		class Meta:
				model = Tag
				fields = '__all__'


class OrderingSerializer(serializers.ModelSerializer):
		customer = CustomerSerializer(read_only=True)
		executor = ExecutorSerializer(read_only=True)
		order = OrderSerializer(read_only=True)
		service = ServiceSerializer(read_only=True)
		class Meta:
				model = Ordering
				fields = '__all__'


class CreateOrderingSerializer(serializers.ModelSerializer):
		customer = CustomerSerializer(read_only=True)
		executor = ExecutorSerializer(read_only=True)
		order = OrderSerializer(read_only=True)
		service = ServiceSerializer(read_only=True)
		class Meta:
				model = Ordering
				fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
		customer = CustomerSerializer(read_only=True)
		executor = ExecutorSerializer(read_only=True)
		class Meta:
				model = Message
				fields = '__all__'


class CreateMessageSerializer(serializers.ModelSerializer):
		customer = CustomerSerializer(read_only=True)
		executor = ExecutorSerializer(read_only=True)
		class Meta:
				model = Message
				fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
		customer = CustomerSerializer(read_only=True)
		executor = ExecutorSerializer(read_only=True)
		severity = serializers.CharField(source='get_severity_display')
		class Meta:
				model = Ticket
				fields = '__all__'


class CreateTicketSerializer(serializers.ModelSerializer):
		customer = CustomerSerializer(read_only=True)
		executor = ExecutorSerializer(read_only=True)
		class Meta:
				model = Ticket
				fields = '__all__'


class ReviewSerializer(serializers.Serializer):
		rating = serializers.CharField(source='get_rating_display')
		class Meta:
			model = Review
			fields = '__all__'


class CreateReviewSerializer(serializers.Serializer):
		class Meta:
			model = Review
			fields = '__all__'


class AuthoringSerializer(serializers.Serializer):
		review = ReviewSerializer(read_only=True)
		author = UserSerializer(read_only=True)
		customer = CustomerSerializer(read_only=True)
		executor = ExecutorSerializer(read_only=True)
		class Meta:
			model = Authoring
			fields = '__all__'


class CreateAuthoringSerializer(serializers.Serializer):
		review = ReviewSerializer(read_only=True)
		author = UserSerializer(read_only=True)
		customer = CustomerSerializer(read_only=True)
		executor = ExecutorSerializer(read_only=True)
		class Meta:
			model = Authoring
			fields = '__all__'
