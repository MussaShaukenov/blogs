from abc import ABC
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from .models import Cards, Categories
from .forms import CardForm, CategoryForm, SearchForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout


class CustomLoginView(LoginView):
    template_name = 'app/login.html'
    success_url = reverse_lazy('card_list')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'app/signup.html'


class CustomLogoutView(LogoutView):
    template_name = 'app/logout.html'
    next_page = reverse_lazy('card_list')


class CardListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Cards
    context_object_name = 'cards'
    template_name = 'app/card_list.html'
    login_url = 'login'


class CardCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Cards
    form_class = CardForm
    template_name = 'app/card_form.html'
    success_url = reverse_lazy('card_list')
    success_message = 'Card created successfully.'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CardUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Cards
    form_class = CardForm
    template_name = 'app/card_form.html'
    success_url = reverse_lazy('card_list')
    success_message = 'Card updated successfully.'
    login_url = 'login'

    def test_func(self):
        card = self.get_object()
        return card.author == self.request.user


class CardDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Cards
    template_name = 'app/card_confirm_delete.html'
    success_url = reverse_lazy('card_list')
    success_message = 'Card deleted successfully.'
    login_url = 'login'

    def test_func(self):
        card = self.get_object()
        return card.author == self.request.user


class CategoryDetailView(DetailView):
    model = Categories
    template_name = 'app/category_detail.html',
    context_object_name = 'categories'


class CardDetailView(DetailView):
    model = Cards
    template_name = 'app/card_detail.html'
    context_object_name = 'card'


class CategoryListView(LoginRequiredMixin, ListView):
    model = Categories
    context_object_name = 'categories'
    template_name = 'app/category_list.html'
    login_url = 'login'


class CategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Categories
    form_class = CategoryForm
    template_name = 'app/category_form.html'
    success_url = reverse_lazy('category_list')
    success_message = 'Category created successfully.'
    login_url = 'login'


class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Categories
    form_class = CategoryForm
    template_name = 'app/category_form.html'
    success_url = reverse_lazy('category_list')
    success_message = 'Category updated successfully.'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_staff


class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView, ABC):
    model = Categories
    template_name = 'app/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')
    success_message = 'Category deleted successfully.'
    login_url = 'login'


class SearchView(TemplateView):
    template_name = 'app/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = SearchForm(self.request.GET)
        results = []
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Cards.objects.filter(name__icontains=query)
        context['form'] = form
        context['results'] = results
        return context