from django.test import TestCase
from article.models import Article,get_upload_file_name
from django.utils import timezone
from time import time
from django.core.urlresolvers import reverse



# Create your tests here.
class ArticleTest(TestCase):
    def create_article(self,title="test article",body="ahsdjokasdhjsak"):
        return Article.objects.create(title=title,body=body,pub_date=timezone.now(),likes=0)

    def test_article_creation(self):
        a= self.create_article()
        self.assertTrue(isinstance(a,Article))
        self.assertEqual(a.__unicode__(),a.title)

    def test_get_upload_file_name(self):
        filename= "cheese.txt"
        path = "uploaded_files/%s_%s" %(str(time()).replace('.','_'),filename)

        created_path = get_upload_file_name(self,filename)

        self.assertEqual(path,created_path)

#test url and view
    def test_articles_list_view(self):
        a = self.create_article()
        url = reverse('views.articles')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code,200)
        self.assertIn(a.title, resp.content)


    def test_article_detail_view(self):
        a = self.create_article()
        url= reverse('views.article',args={a.id})
        resp= self.client.get(url)

        self.assertEqual(url, a.get_absolute_url())
        self.assertEqual(resp.status_code,200)
        self.assertIn(a.title,resp.content)
