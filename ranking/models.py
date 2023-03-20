from django.db import models

# Create your models here.
class MovieTournament(models.Model):
    """トーナメントモデル"""
    name = models.CharField(verbose_name='トーナメント名', max_length=30, null=False, blank=False)
    comment = models.CharField(verbose_name='トーナメントに関する補足', max_length=100, null=False, blank=True)
    category = models.CharField(verbose_name='カテゴリー', max_length=30, null=False, blank=False)
    link_list_str = models.TextField(verbose_name='動画リンク')
    thumbnail_list_str = models.TextField(verbose_name='サムネ')
    title_list_str = models.TextField(verbose_name='タイトル')
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    @property
    def link_list(self):
        return self.link_list_str.split(',')

    @link_list.setter
    def link_list(self, value):
        self.link_list_str = ','.join(value)

    @property
    def thumbnail_list(self):
        return self.thumbnail_list_str.split(',')

    @thumbnail_list.setter
    def thumbnail_list(self, value):
        self.thumbnail_list_str = ','.join(value)

    @property
    def title_list(self):
        return self.title_list_str.split(',')

    @title_list.setter
    def title_list(self, value):
        self.title_list_str = ','.join(value)

    def __str__(self):
        return self.name