from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import OrderItem, Order
from django.urls import reverse_lazy, reverse
from django.forms import inlineformset_factory
from .forms import OrderItemEditForm
from django.db import transaction
from basketapp.models import Basket
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.dispatch import receiver
from django.db.models.signals import pre_save, pre_delete

class OrderList(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, is_active = True)

class OrderCreate(CreateView):
    model = Order
    success_url = reverse_lazy('order:list')
    fields = []

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemEditForm, extra=1)
        if self.request.POST:
            formset = OrderFormSet(self.request.POST)
        else:
            basket_items = Basket.objects.filter(user = self.request.user)
            if len(basket_items):
                OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemEditForm, extra=len(basket_items))
                formset = OrderFormSet()
                for num, form in enumerate(formset.forms):
                    form.initial['product'] = basket_items[num].product
                    form.initial['quantity'] = basket_items[num].quantity
                    form.initial['price'] = basket_items[num].product.price
                basket_items.delete()
            else:
                formset = OrderFormSet()
        data['orderitems'] = formset
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems  = context['orderitems']

        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()

        if self.object.get_total_cost() == 0:
            self.object.delete()

        return super().form_valid(form)

class OrderUpdate(UpdateView):
    model = Order
    success_url = reverse_lazy('order:list')
    fields = []

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemEditForm, extra=1)
        if self.request.POST:
            formset = OrderFormSet(self.request.POST,instance=self.object)
        else:
            formset = OrderFormSet(instance=self.object)
            for form in formset.forms:
                if form.instance.pk:
                    form.initial['price'] = form.instance.product.price
        data['orderitems'] = formset
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems  = context['orderitems']

        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()

        if self.object.get_total_cost() == 0:
            self.object.delete()

        return super().form_valid(form)

class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('order:list')

class OrderRead(DetailView):
    model = Order

def forming_complete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.status = Order.SENT_TO_PROCEED
    order.save()
    return HttpResponseRedirect(reverse('order:list'))

# @receiver(pre_save,sender=Basket)
# @receiver(pre_save,sender=OrderItem)
# def product_quantity_update_save(sender, update_fields, instance, **kwargs):
#     if instance.pk:
#         instance.product.quantity -= instance.quantity - instance.get_item(instance.pk).quantity
#     else:
#         instance.product.quantity -= instance.quantity
#     instance.product.save()
#
# @receiver(pre_delete,sender=Basket)
# @receiver(pre_delete,sender=OrderItem)
# def product_quantity_update_delete(sender, update_fields, instance, **kwargs):
#     instance.product.quantity += instance.quantity
#     instance.product.save()