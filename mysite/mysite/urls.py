from django.contrib import admin
#
from django.urls import include, path

urlpatterns = [
    #svaki url koji pocinje s polls/, trebalo bi proslijediti polls aplikaciji(polls.urls je referenca)
    #polls/hello -> ovdje django govori da svi zahtjevi koji pocinju s polls treba preusmjeriti u aplikaciju polls, gdje ce biti obradeni. Kada preusmjerava u aplikaciju tehnicki "odreze" ovaj dio polls/ i proslijedi hello u aplikaciju
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
