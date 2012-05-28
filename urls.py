from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tutorial.views.home', name='home'),
    # url(r'^tutorial/', include('tutorial.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
        
    #url(r'^$', 'blog.views.index', name='home'),
    url(
        r'^blog/view/(?P<slug>[^\.]+)', 
        'blog.views.view_post', 
        name='view_blog_post'),
	url(
        r'^blog/add/blog', 
        'blog.views.add_blog', 
        name='add_blog_post'),
    url(
        r'^blog/category/(?P<slug>[^\.]+)', 
        'blog.views.view_category', 
        name='view_blog_category'),
	
	
)

urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns('wordconfuse.views',
        (r'^$', TemplateView.as_view(template_name="index.html")),
        url(r'^get_words$', 'get_words', name='get_words'),
        url(r'^gameover$', 'gameover', name='gameover'),
        url(r'^new_hs$', 'new_hs', name='new_hs'),
        url(r'^hs$', 'hs', name='hs'),
            
        )

