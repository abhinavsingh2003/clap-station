from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path('postdelete/<int:id>',views.postdelete,name='postdelete'),
    path('postedit/<int:id>',views.postedit,name='postedit'),
    path('postupdate/<str:id>',views.postupdate,name='postupdate'),
    path('groups/', views.groups_page, name='groups'),
    path('groupdelete/<int:id>',views.groupdelete,name='groupdelete'),
    path('groupedit/<int:id>',views.groupedit,name='groupedit'),
    path('groupupdate/<str:id>',views.groupupdate,name='groupupdate'),
    path('bands/', views.bands_page, name='bands'),
    path('event_details/', views.event_details, name='event_details'),
    path('deletelist/<int:id>',views.deletelist,name='deletelist'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<str:id>',views.update,name='update'),
    path('academies/', views.academies_page, name='academies'),
    path('events/', views.events_page, name='events'),
    path('artists/', views.artists_page, name='artists'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),
    path('signup/', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('profile/', views.profile_page, name='profile'),
    path('jammingstation/', views.jammingstation_page, name='jammingstation'),
    
    
    path('like/',views.like_post,name='like-post'),
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

