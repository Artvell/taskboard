"""Файл с классами, отвечающими за отображение моделей в админ-панели Django"""
from django.contrib import admin
import main.models as models
from main.forms import CustomBIOForm, CustomEntityCommentsForm, CustomEntityForm
from main.functions import create_other_data_list
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class BIOAdmin(admin.ModelAdmin):
    """отображает модель BIO в админ-панели.
    Изменен вывод/сохранение полей aliases,low_quality_aliases,alternative_spelling
    """
    list_display = [field.name for field in models.BIO._meta.fields]
    form = CustomBIOForm
    def change_view(self, request, object_id, form_url='', extra_context=None):
        data = models.BIO.objects.get(id=object_id)
        all_data = {
            "aliases":data.aliases,
            "low_quality_aliases":data.low_quality_aliases,
            "alternative_spelling":data.alternative_spelling
        }
        all_data = {k: v for k, v in all_data.items() if (v != {} and v!=[])}
        extra = extra_context or {}
        extra['all_data'] = all_data
        return super(BIOAdmin, self).change_view(request, object_id,
                                                    form_url, extra_context=extra)

class CategoryAdmin(admin.ModelAdmin):
    """отображает модель Category в админ-панели"""
    list_display = [field.name for field in models.Category._meta.fields]

class CountryAdmin(admin.ModelAdmin):
    """отображает модель Country в админ-панели"""
    list_display = [field.name for field in models.Country._meta.fields]

class EntityAdmin(SummernoteModelAdmin):
    """отображает модель Entity в админ-панели.
    Изменен вывод/сохранение полей external_sources,locations
    """
    form = CustomEntityForm
    summernote_fields = ('further_information',)
    filter_horizontal = ('countries',"keywords")
    list_display = [
        field.name for field in models.Entity._meta.fields if field.name != "further_information"
        ]
    def change_view(self, request, object_id, form_url='', extra_context=None):
        data = models.Entity.objects.get(id=object_id)
        all_data = {
            "external_sources":data.external_sources,
            "locations":data.locations
        }
        all_data = {k: v for k, v in all_data.items() if (v != {} and v!=[])}
        extra = extra_context or {}
        extra['all_data'] = all_data
        return super(EntityAdmin, self).change_view(request, object_id,
                                                    form_url, extra_context=extra)

class KeywordsAdmin(admin.ModelAdmin):
    """отображает модель Keywords в админ-панели"""
    list_display = [field.name for field in models.Keywords._meta.fields]

class PassportAdmin(admin.ModelAdmin):
    """отображает модель Passport в админ-панели"""
    list_display = [field.name for field in models.Passport._meta.fields]

class SubcategoryAdmin(admin.ModelAdmin):
    """отображает модель Subcategory в админ-панели"""
    list_display = [field.name for field in models.Subcategory._meta.fields]

class L3CommentAdmin(admin.ModelAdmin):
    """отображает модель L3Comment в админ-панели"""
    list_display = [field.name for field in models.L3Comment._meta.fields]

class CommentsAdmin(admin.ModelAdmin):
    """отображает модель в админ-панели
    Изменен вывод/сохранение полей passports,countries, keywords
    Отключена возможность создания нового экземпляра модели в админке
    """
    form = CustomEntityCommentsForm
    change_form_template = 'admin/main/entitycomments/change_form.html'
    list_display = [field.name for field in models.EntityComments._meta.fields]
    def has_add_permission(self, request):
        return False
    def change_view(self, request, object_id, form_url='', extra_context=None):
        data = models.EntityComments.objects.get(id=object_id)
        all_errors = {
            "passports":create_other_data_list(
                data.passports,models.Passport.objects.filter(entity=data.entity)
                ),
            "countries":create_other_data_list(
                data.countries,data.entity.countries.all()
                ),
            "keywords":create_other_data_list(
                data.keywords,data.entity.keywords.all()
                )
        }
        extra = extra_context or {}
        extra['all_errors'] = all_errors
        return super(CommentsAdmin, self).change_view(request, object_id,
                                                    form_url, extra_context=extra)


admin.site.register(models.BIO,BIOAdmin)
admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Country,CountryAdmin)
admin.site.register(models.Entity,EntityAdmin)
admin.site.register(models.EntityComments,CommentsAdmin)
admin.site.register(models.Keywords,KeywordsAdmin)
admin.site.register(models.Passport,PassportAdmin)
admin.site.register(models.Subcategory,SubcategoryAdmin)
admin.site.register(models.L3Comment,L3CommentAdmin)
