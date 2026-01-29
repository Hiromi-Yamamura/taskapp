from django.db import models

CATEGORY = (('1','下版予定'),('2','下版済み'),('3','作業中'),('4','最終確認中'),('5','作業完了'))
CATEGORY2 = (('1','下版作業中'),('2','PDF待ち'),('3','PDF作成済み'),('4','先方確認中'),('5','三協美術に依頼'))

class Book(models.Model):
  title = models.CharField(max_length=300)
  text=models.TextField(null=True, blank=True)
  thumbnail = models.ImageField(null=True, blank=True)
  category = models.CharField(
    max_length=100,
    choices=CATEGORY,
    null=True, blank=True
  )
  category2 = models.CharField(
    max_length=100,
    choices=CATEGORY2,
    null=True, blank=True
  )
  type = models.IntegerField(null=True, blank=True)
  status = models.IntegerField(null=True, blank=True)
  stage = models.IntegerField(null=True, blank=True)
  operator = models.IntegerField(null=True, blank=True)
  estimated_hours = models.CharField(max_length=50,null=True, blank=True)
  due_date = models.CharField(max_length=50,null=True, blank=True)
  percent = models.IntegerField(null=True, blank=True)
  comment = models.TextField(null=True, blank=True)
  order_num = models.IntegerField(null=True, blank=True)
  delete_flg = models.IntegerField(default=0)
  created_user = models.IntegerField(null=True, blank=True)
  updated_user = models.IntegerField(null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True,null=True, blank=True)
  
  def __str__(self):
    return self.title
