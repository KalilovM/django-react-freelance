from django.db import models
from django.contrib.auth.models import User


class Executor(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return '{}'.format(self.user)

class Customer(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return '{}'.format(self.user)

class Service(models.Model):
	SERVICE_TYPES = [
		('1', 'Фронт-енд'),
		('2', 'Бэк-енд'),
		('3', 'Дизайн'),
		('4', 'Разработка'),
		('5', 'Тестирование'),
		('6', 'Разное'),
]
	executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	description = models.TextField()
	price = models.IntegerField()
	service_type = models.CharField(default='1',max_length=1, choices=SERVICE_TYPES)
	
	def __str__(self):
		return '{} - {}, price: {}'.format(self.name, self.get_service_type_display(), self.price)


class Order(models.Model):
	ORDER_TYPE = [
		('1', 'Фронт-енд'),
		('2', 'Бэк-енд'),
		('3', 'Дизайн'),
		('4', 'Разработка'),
		('5', 'Тестирование'),
		('6', 'Разное'),
]
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	description = models.TextField()
	price = models.IntegerField()
	order_type = models.CharField(default='1',max_length=1, choices=ORDER_TYPE)
	
	def __str__(self):
		return '{} - {}, price: {}'.format(self.name, self.get_service_type_display(), self.price)


class Ordering(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
	service = models.ForeignKey(Service, on_delete=models.CASCADE)
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	order_date = models.DateTimeField(auto_now_add=True)
	deadline = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{} - {} customer: {} - executor: {}'.format(self.order_date,self.deadline,self.customer, self.executor)

class Tag(models.Model):
	service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True)
	order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True)
	name = models.CharField(max_length=100)

	def __str__(self):
		return '{}'.format(self.name)

class Message(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
	msg_date = models.DateTimeField(auto_now_add=True)
	is_edited = models.BooleanField(default=False)
	description = models.TextField()

class Ticket(models.Model):
	SEVERITIES = [
		('1', 'Низкий'),
		('2', 'Средний'),
		('3', 'Высокий'),
	]
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
	severity = models.CharField(default='1',max_length=1, choices=SEVERITIES)
	description = models.TextField()
	ticket_date = models.DateTimeField(auto_now_add=True)
	is_resolved = models.BooleanField(default=False)

	def __str__(self):
		return '{} - {}, Is resolved: {}'.format(self.get_severity_display(),self.ticket_date,  self.is_resolved)

class Review(models.Model):
	RATING_FILLED = [
		('1', '1'),
		('2', '2'),
		('3', '3'),
		('4', '4'),
		('5', '5'),
	]
	rating = models.CharField(default='1',max_length=1, choices=RATING_FILLED)
	description = models.TextField()

class Authoring(models.Model):
	review = models.ForeignKey(Review, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
	review_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{}, {}'.format(self.author, self.review_date)