from django.db import models
from django.forms import ModelForm


class ExcelEntries(models.Model):
    name=models.CharField(verbose_name='Имя',default="None",max_length=50)
    desc=models.TextField(verbose_name='Описание',default="None",max_length=100)
    file=models.FileField(upload_to='excel_files',verbose_name='Файл для загрузки')

    def __str__(self):
        return self.name.__str__()+"    -    "+self.file.name


class LoadForm(ModelForm):
    class Meta:
        model = ExcelEntries
        fields = ['name','desc','file']

# Create your models here.
