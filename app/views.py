from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic import View,CreateView, ListView
from .models import MusicModel,MovieModel
from .forms import MusicForm,MovieForm
from django.db.models import Q



class Index(View):
    def get(self,request):
        return  render(request,"index.html")



class Upload(View):
    def get(self, request):
        return render(request,"upload.html",{"mf":MovieForm(),"msf":MusicForm()})

    def post(self,request):
        b = request.POST["b1"]

        if b == 'movie':
            mf = MovieForm(request.POST,request.FILES)
            if mf.is_valid():
                mf.save()
                messages.success(request,"The Song is uploaded...")
                return redirect("upload")
            else:
                return render(request, "upload.html", {"mf": mf, "msf": MusicForm()})

        else:
            msf = MusicForm(request.POST, request.FILES)
            if msf.is_valid():
                msf.save()
                return redirect("upload")
            else:
                return render(request, "upload.html", {"mf": MovieForm, "msf": msf})



class View_all(View):
    def get(self,request):
        a = MusicModel.objects.all()
        return render(request,"view_all.html",{"all":a})


class Albums(ListView):
    template_name = "albums.html"
    model = MovieModel
    paginate_by = 3


class Artists(View):
    def get(self,request):
        m = MusicModel.objects.values('artist',)
        l = []
        for x in m:
            for y,z in x.items():
                l.append(z)
        mylist = list(dict.fromkeys(l))

        return render(request,"artist.html",{"artists":mylist})


class One_album(View):
    def get(self,request):
        m = request.GET['m']
        a = MusicModel.objects.filter(album_name_id=m)
        b = MovieModel.objects.get(name=m)
        return render(request,"one_album.html",{"album":a,"image":b,})


class One_song(View):
    def get(self,request):
        s = request.GET["s"]
        s1 = MusicModel.objects.get(songid=s)
        return render(request,"one_song.html",{"data":s1})


class One_artist(View):
    def get(self,request):
        a = request.GET["a"]
        ar = MusicModel.objects.filter(artist=a)
        return render(request,"one_artist.html",{"data":ar,"artist":a})

def search(request):
    s = request.POST["s1"]
    if s:
        src = MusicModel.objects.filter(Q(album_name__name__icontains=s) | Q(artist__icontains=s) | Q(tittle__icontains=s))
        if src:
            return render(request, "search.html", {"all": src})
        else:
            return render(request,"search.html",{"mes":" Sorry we couldn't find any matches for","sr": s})
    else:
        return render(request, "search.html", {"mes":"Enter something to search mp3..."})


class OpenDelete(View):
    def get(self,request):
        a = MusicModel.objects.all()
        return  render(request,"open_delete.html",{"all":a})


class Delete(View):
    def get(self,request):
        s = request.GET["s"]
        a = MusicModel.objects.get(songid=s)
        return  render(request,"delete.html",{"data":a})
    def post(self,request):
        b = request.POST["b1"]
        i = request.POST["id"]
        if b == 'confirm':
            MusicModel.objects.get(songid=i).delete()
            return redirect('o_delete')
        else:
            return redirect('o_delete')


class AdminLogin(View):
    def get(self,request):
        return render(request,"a_login.html")
    def post(self,request):
        user=request.POST.get('username')
        password=request.POST.get('password')
        if user=='rajesh' and password=='1234':
            request.session['user_id']=user
            return redirect('logincheck')
        else:
            messages.error(request,"The Username and Password Invalid...")
            return redirect('a_login')


def logincheck(request):
    res=request.session.get('user_id',None)
    if res:
        return redirect('upload')
    else:
        return redirect('a_login')


def Logout(request):
    del request.session['user_id']
    return redirect('logincheck')