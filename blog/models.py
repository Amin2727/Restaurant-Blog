from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Blog(models.Model):
    """This model is related to post creation."""

    title = models.CharField(_("عنوان"),max_length=50)
    description = models.CharField(_("توضیحات"),max_length=100)
    content = RichTextField(_("متن"))
    created_at = models.DateTimeField(_("زمان انتشار"), default=timezone.now)
    author = models.ForeignKey(User, verbose_name=_("نویسنده"), on_delete=models.CASCADE)
    image = models.ImageField(_("تصویر"), upload_to="blogs/")
    category = models.ForeignKey("Category", related_name="blog", verbose_name=_("دسته بندی"), on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag", verbose_name=_("تگ ها"), related_name="blogs")

    def __str__(self):
        return self.title



class Category(models.Model):
    """This model is related to the category of posts."""

    title = models.CharField(_("عنوان"), max_length=50)
    slug = models.SlugField(_("عنوان لاتین"))
    published_at = models.DateTimeField(_("تاریخ انتشار"), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title



class Tag(models.Model):
    """This model is related to post tags."""

    title = models.CharField(_("عنوان"), max_length=50)
    slug = models.SlugField(_("عنوان لاتین"))
    published_at = models.DateTimeField(_("تاریخ انتشار"), auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(_("تاریخ بروزرسانی"), auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title
    


class Comment(models.Model):
    """This model is related to posting comments on posts."""

    blog = models.ForeignKey("Blog", verbose_name=_("مقاله"), related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(_("نام کاربر"), max_length=100)
    email = models.EmailField(_("ایمیل"), max_length=254)
    message = models.TextField(_("متن نظر"))
    date = models.DateField(_("تاریخ انتشار"), auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name