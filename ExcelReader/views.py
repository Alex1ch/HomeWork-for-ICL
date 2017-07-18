from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import DetailView
from ExcelReader import models
import xlrd

def mainPage(request):
    return HttpResponseRedirect('excelreader/loadfile/')

def loadView(request):
    if request.method=='GET':
        context = {'form':models.LoadForm(),'error_msg':""}
        return render(request, 'loadpage.html', context)
    if request.method=='POST':
        form=models.LoadForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data['file'].name[::-1][:4]=='xslx' or form.cleaned_data['file'].name[::-1][:3]=='slx':
                instance = form.save()
                xcl_file = xlrd.open_workbook(instance.file.path)
                sheet=xcl_file.sheet_by_index(0)
                if sheet.nrows<10 or sheet.ncols<2:
                    instance.delete()
                    return HttpResponse("Excel файл содержит менее 10-ти строк или менее 2-х столбцов")

                coordsstring=""
                colx=sheet.col_values(0)
                coly=sheet.col_values(1)

                for i in range(sheet.nrows):
                    if type(colx[i]) is not float:
                        instance.delete()
                        return HttpResponse("Excel файл содержит не числовые значения или количество строк в столбцах не совпадает")

                    if type(coly[i]) is not float:
                        instance.delete()
                        return HttpResponse("Excel файл содержит не числовые значения или количество строк в столбцах не совпадает")

                    if i!=0:
                        coordsstring += "," + str(colx[i])
                    else:
                        coordsstring += str(colx[i])
                coordsstring+="\n"
                for i in range(sheet.nrows):
                    if i!=0:
                        coordsstring += "," + str(coly[i])
                    else:
                        coordsstring += str(coly[i])
                return HttpResponse("Принято (id="+str(instance.id)+")"+". Координаты: \n" + coordsstring)
            return HttpResponse("Не верный формат файла! ("+form.cleaned_data['file'].name+")")
        return HttpResponse("Не удалось загрузить файл!")


def get_list(request):
    response="";
    for object in models.ExcelEntries.objects.all():
        response = response + str(object.id)+"/*/"+str(object.desc)+"/*/"+str(object.name)+"\n"
    return HttpResponse(response)


def get_graph(request,*args,**kwargs):
    id=kwargs['id']
    instance=models.ExcelEntries.objects.get(id=id)
    xcl_file = xlrd.open_workbook(instance.file.path)
    sheet = xcl_file.sheet_by_index(0)

    coordsstring = ""
    colx = sheet.col_values(0)
    coly = sheet.col_values(1)

    for i in range(sheet.nrows):
        if i != 0:
            coordsstring += "," + str(colx[i])
        else:
            coordsstring += str(colx[i])
    coordsstring += "\n"
    for i in range(sheet.nrows):
        if i != 0:
            coordsstring += "," + str(coly[i])
        else:
            coordsstring += str(coly[i])
    return HttpResponse(coordsstring)

# Create your views here.
