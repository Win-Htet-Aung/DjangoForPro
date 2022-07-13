from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView
from django.http.response import HttpResponseRedirect

from .urls import urlpatterns

# Create your tests here.
print(urlpatterns)
# test_url = urlpatterns[0]
# print(test_url.name)

class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_hompage_contains_correct_html(self):
        self.assertContains(self.response, 'home page')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'This is not on the page!')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)

class UrlsTests(SimpleTestCase):
    def test_urls(self):
        for pattern in urlpatterns:
            url = reverse(pattern.name)
            print(f"\ntesting {url}", end = '')
            response = self.client.get(url)
            if not isinstance(response, HttpResponseRedirect):
                self.assertEqual(response.status_code, 200)
            else:
                print(f"{url} is redirecting to {response.url}")
    
    def test_post_req(self):
        url = reverse('new_home')
        data = {
            'color': 'red',
        }
        response = self.client.post(url, data)
        print(response, dir(response))
        self.assertEqual(1, 1)

