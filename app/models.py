from django.db import models

class MovieModel(models.Model):
    name = models.CharField(primary_key = True,max_length=30)
    album_image = models.ImageField(upload_to="album_images/")

    def __str__(self):
        return self.name

class MusicModel(models.Model):
    songid = models.AutoField(primary_key=True)
    tittle = models.CharField(max_length=60)
    artist = models.CharField(max_length=30)
    song_image = models.ImageField(upload_to="song_images/")
    song = models.FileField(upload_to="songs/")
    album_name = models.ForeignKey(MovieModel,on_delete=models.CASCADE)





