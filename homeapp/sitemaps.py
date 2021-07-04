from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from user.models import post
class StaticViewSitemap(Sitemap):
    def items(self):
        return['home_page']
    
    def location(self, item):
        return reverse(item)


class blog_view(Sitemap):
    def items(self):
        all_pages = list()
        all_posts = post.objects.all()
        for i in all_posts:
            url = f'/blog_view/?post_id={i.id}&class=blog_view'
            all_pages.append(url)
        return all_pages
    def location(self, item):
        return item
class login(Sitemap):
    def items(self):
        return ['login']
    def location(self, item):
        return reverse(item)


class logout(Sitemap):
    def items(self):
        return ['logout']
    def location(self, item):
        return reverse(item)




class register(Sitemap):
    def items(self):
        return ['register']
    def location(self, item):
        return reverse(item)
