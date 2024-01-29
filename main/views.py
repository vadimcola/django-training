from django.forms import FileField, inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import *

from main.forms import ProductForm, VersionForm
from main.models import Product, Blog, Version


class ProductListView(generic.ListView):
    model = Product


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'main/product_detail.html'


class ProductCreateView(generic.CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:prod_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductUpdateView(generic.UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:prod_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(generic.DeleteView):
    model = Product
    success_url = reverse_lazy('main:prod_list')
    template_name = 'main/product_confirm_delete.html'


class BlogListView(generic.ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'main/blog_detail.html'
    slug_url_kwarg = 'the_slug'
    slug_field = 'slug'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class BlogCreateView(generic.CreateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'picture', 'is_published')
    success_url = reverse_lazy('main:blog_list')
    template_name = 'main/blog_form.html'


class BlogUpdateView(generic.UpdateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'picture', 'is_published')
    template_name = 'main/blog_form.html'
    slug_url_kwarg = 'the_slug'
    slug_field = 'slug'

    def get_success_url(self):
        return reverse('main:blog_item', kwargs={'the_slug': self.object.slug})


class BlogDeleteView(generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('main:blog_list')
    template_name = 'main/blog_confirm_delete.html'
    slug_url_kwarg = 'the_slug'
    slug_field = 'slug'
