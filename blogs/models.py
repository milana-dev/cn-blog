from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



"""
OnetoOneField - Yeni bir userin bir blogu ola biler
ManytoMany de yeni cedvel yaranir
ForeignKey - Yeni bir userin bir nece hesabi ola biler
ManytoManyField - Yeni coxlu userin coxlu hesabi ola biler
on_delete - odurki,  meselen men instada profilimi silirem,ama sekillerim qalir axi.yeni bu sekillerimi neynesin?
onda uje yazirsan models.cascade .bu nedi? yeni profili silende sekilleri de tam sil, yeni bir sozle baza seviyyesinde yox ele.
set_null odur ki, yeni profil silinecek  ama melumatlari qalacaq.Meselen sen instadan profilini silirsen,  ama senin yazisalarin qalir niye? set_null-a gore.
ve sen qayidib hemin sehifeni berpa ede bilmersen artiq. 
"""

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'




class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=50) # ----> yazi ucun limit var
    about = models.TextField()  #----> yazi  ucun limit yoxdu
    published_date = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        try:
            return f'{self.author.username} --- {self.title}'
        except:
            return f'null --- {self.title}'
        
    
