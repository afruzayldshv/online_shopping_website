from django.db import models
import uuid
from django.contrib.auth.models import User

class Category(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,verbose_name='Id')
    name=models.CharField(max_length=100,verbose_name='Type of category')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'

class Subcategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='Id')
    name = models.CharField(max_length=100, verbose_name='Subcategory')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='subcategories',verbose_name='Category')

    def __str__(self):
        return f'{self.category.name}-{self.name}'

    class Meta:
        verbose_name='Subcategory'
        verbose_name_plural='Subcategories'

class Good(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='Id')
    name = models.CharField(max_length=100, verbose_name='Name of product')
    price=models.DecimalField(max_digits=10,decimal_places=3,verbose_name='Price')
    description=models.TextField(null=True,blank=True,verbose_name='Description of the good')
    is_available=models.BooleanField(default=True,verbose_name='In stock')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE,verbose_name='Subcategory',null=True,blank=True)
    image = models.ImageField(upload_to='goods/previews/', null=True, blank=True, verbose_name='Image')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Good'
        verbose_name_plural = 'Goods'

class Comment(models.Model):
    text=models.TextField(verbose_name='text')
    author=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='author')
    good=models.ForeignKey(Good,on_delete=models.CASCADE,verbose_name='good',null=True)
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='date/time')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

class Basket(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='basket')

    def __str__(self):
        return f'Basket of {self.user}'

    class Meta:
        verbose_name = 'Basket'
        verbose_name_plural = 'Baskets'

class BasketItem(models.Model):
    basket=models.ForeignKey(Basket,on_delete=models.CASCADE,related_name='basket_items')
    good=models.ForeignKey(Good,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)

    class Meta:
        unique_together='basket','good'

class Saved(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='saved')



class SavedGood(models.Model):
    saved=models.ForeignKey(Saved,on_delete=models.CASCADE,related_name='saved_goods')
    good=models.ForeignKey(Good,on_delete=models.CASCADE)

    class Meta:
        unique_together='saved','good'









