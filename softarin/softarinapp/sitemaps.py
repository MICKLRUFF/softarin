from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['home', 'about', 'contact', 'services', 'projects', 'service', 'project']  # Назви ваших URL-ім'я

    def location(self, item):
        return reverse(item)