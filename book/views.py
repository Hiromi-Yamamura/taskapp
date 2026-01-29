from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView,)
from django.contrib.auth.decorators import login_required
from .models import Book
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
import json

class ListBookView(LoginRequiredMixin, ListView):
  template_name='book/index.html'
  model = Book

class DetailBookView(LoginRequiredMixin, DetailView):
  template_name = 'book/book_detail.html'
  model = Book
  
class CreateBookView(LoginRequiredMixin, CreateView):
  template_name = 'book/book_create.html'
  model = Book
  fields = ('title', 'type', 'status', 'stage', 'operator', 'estimated_hours', 'due_date', 'percent', 'comment', 'order_num', 'created_user')
  success_url = reverse_lazy('list-book')

class UpdateBookView(LoginRequiredMixin, UpdateView):
  template_name = 'book/book_update.html'
  model = Book
  fields = ('title', 'text', 'category', 'thumbnail')
  success_url = reverse_lazy('list-book')
  
class DeleteBookView(LoginRequiredMixin, DeleteView):
  template_name = 'book/book_confirm_delete.html'
  model = Book
  success_url = reverse_lazy('list-book')

@login_required(login_url='/login/')
def index_view(request):
  print('index_view is called')
  user_id = request.user.id

  object_list = Book.objects.all().filter(delete_flg=0).order_by('order_num')
  json_encode = list(object_list.values())
  return render(request,'book/index.html',{'object_list':json_encode})

@csrf_exempt # 必要に応じて適切にCSRF対策を実施
def save_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_item = Book(type=data['type'], title=data['title'], stage=data['stage'], status=data['status'], operator=data['operator'], percent=data['percent'], due_date=data['due_date'], estimated_hours=data['estimated_hours'], comment=data['comment'], created_user=data['created_user'], )
        new_item.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)
  
def edit_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        obj = Book.objects.get(id=data['id'])
        obj.stage = data['stage']
        obj.status = data['status']
        obj.operator = data['operator']
        obj.percent = data['percent']
        obj.comment = data['comment']
        obj.updated_user = data['updated_user']
        obj.save() # データベースの更新
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

@csrf_exempt
def update_stage(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print('stage_data')
        print(data)
        obj = Book.objects.get(id=data['id'])
        obj.stage = data['stage']
        obj.save() # データベースの更新
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'}, status=400)
  
@csrf_exempt
def update_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        x = 1
        for id in data['id']:
          obj = Book.objects.get(id=id)
          obj.order_num = x
          obj.save() # データベースの更新
          x += 1
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'}, status=400)
  
@csrf_exempt
def delete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        obj = Book.objects.get(id=data['id'])
        obj.delete_flg = 1
        obj.save() # データベースの更新
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'}, status=400)
