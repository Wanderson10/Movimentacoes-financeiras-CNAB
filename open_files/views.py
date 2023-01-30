from django.http import HttpResponse
import locale
from django.shortcuts import render
from .models import File



def showfile(request):
     if request.method == "POST":

        if not dict(request.FILES):
            return HttpResponse("no data :(")

        data = dict(request.FILES)["file"][0]

        for line in data.readlines():
            decode = line.decode("utf8")
            new_file = File()
            new_file.type = decode[0]
            new_file.date = decode[1:9]
            locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
            new_file.value = locale.currency(
                (int(decode[9:19]) / 100),
                grouping=True,
            )
            new_file.cpf = decode[19:30]
            new_file.card = decode[30:42]
            new_file.hour = decode[42:48]
            new_file.store_owner = decode[48:62].strip()
            new_file.store_name = decode[62:81][0:-1].strip()

            new_file.save()

        all_file = File.objects.all()

        return render(
            request, "html_render/data.html", {"all-file": all_file}
        )

     return render(request, "open_files/index.html")
   
    
      
    
