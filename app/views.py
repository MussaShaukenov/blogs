from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Cards, Categories
from .forms import CardForm, SearchForm, CategoryForm


class CardListView(ListView):
    model = Cards
    template_name = 'app/card_list.html'
    context_object_name = 'cards'


class CardCreateView(CreateView):
    model = Cards
    form_class = CardForm
    template_name = 'app/card_form.html'
    success_url = reverse_lazy('card_list')


class CardUpdateView(UpdateView):
    model = Cards
    form_class = CardForm
    template_name = 'app/card_form.html'
    success_url = reverse_lazy('card_list')

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Cards, pk=pk)


class CardDeleteView(DeleteView):
    model = Cards
    template_name = 'app/card_confirm_delete.html'
    success_url = reverse_lazy('card_list')

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Cards, pk=pk)


class CardDetailView(DetailView):
    model = Cards
    template_name = 'app/card_detail.html'
    context_object_name = 'card'


class SearchView(View):
    template_name = 'app/search.html'

    def get(self, request, *args, **kwargs):
        form = SearchForm(request.GET)
        results = []
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Cards.objects.filter(title__icontains=query)
        context = {'form': form, 'results': results}
        return render(request, self.template_name, context)


class CategoryListView(ListView):
    model = Categories
    template_name = 'app/category_list.html'
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Categories
    template_name = 'app/category_detail.html',
    context_object_name = 'categories'


class CategoryCreateView(CreateView):
    model = Categories
    form_class = CategoryForm
    template_name = 'app/category_form.html'
    success_url = reverse_lazy('card_list')


class CategoryUpdateView(UpdateView):
    model = Categories
    form_class = CategoryForm
    template_name = 'app/category_form.html'
    success_url = reverse_lazy('category_list')

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Cards, pk=pk)


class CategoryDeleteView(DeleteView):
    model = Categories
    template_name = 'app/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Cards, pk=pk)
