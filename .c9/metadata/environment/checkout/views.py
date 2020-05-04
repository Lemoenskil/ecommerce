{"filter":false,"title":"views.py","tooltip":"/checkout/views.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.shortcuts import render","","# Create your views here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":24,"column":9},"action":"insert","lines":["from django import forms","from .models import Order","","","class MakePaymentForm(forms.Form):","","    MONTH_CHOICES = [(i, i) for i in range(1, 12)]","    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]","","    credit_card_number = forms.CharField(label='Credit card number', required=False)","    cvv = forms.CharField(label='Security code (CVV)', required=False)","    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)","    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)","    stripe_id = forms.CharField(widget=forms.HiddenInput)","","","class OrderForm(forms.ModelForm):","","    class Meta:","        model = Order","        fields = (","            'full_name', 'phone_number', 'country', 'postcode',","            'town_or_city', 'street_address1', 'street_address2',","            'county'","        )"]}],[{"start":{"row":0,"column":0},"end":{"row":24,"column":9},"action":"remove","lines":["from django import forms","from .models import Order","","","class MakePaymentForm(forms.Form):","","    MONTH_CHOICES = [(i, i) for i in range(1, 12)]","    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]","","    credit_card_number = forms.CharField(label='Credit card number', required=False)","    cvv = forms.CharField(label='Security code (CVV)', required=False)","    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)","    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)","    stripe_id = forms.CharField(widget=forms.HiddenInput)","","","class OrderForm(forms.ModelForm):","","    class Meta:","        model = Order","        fields = (","            'full_name', 'phone_number', 'country', 'postcode',","            'town_or_city', 'street_address1', 'street_address2',","            'county'","        )"],"id":3},{"start":{"row":0,"column":0},"end":{"row":60,"column":145},"action":"insert","lines":["from django.shortcuts import render, get_object_or_404, reverse, redirect","from django.contrib.auth.decorators import login_required","from django.contrib import messages","from .forms import MakePaymentForm, OrderForm","from .models import OrderLineItem","from django.conf import settings","from django.utils import timezone","from products.models import Product","import stripe","","# Create your views here.","stripe.api_key = settings.STRIPE_SECRET","","","@login_required()","def checkout(request):","    if request.method == \"POST\":","        order_form = OrderForm(request.POST)","        payment_form = MakePaymentForm(request.POST)","","        if order_form.is_valid() and payment_form.is_valid():","            order = order_form.save(commit=False)","            order.date = timezone.now()","            order.save()","","            cart = request.session.get('cart', {})","            total = 0","            for id, quantity in cart.items():","                product = get_object_or_404(Product, pk=id)","                total += quantity * product.price","                order_line_item = OrderLineItem(","                    order=order,","                    product=product,","                    quantity=quantity","                )","                order_line_item.save()","            ","            try:","                customer = stripe.Charge.create(","                    amount=int(total * 100),","                    currency=\"EUR\",","                    description=request.user.email,","                    card=payment_form.cleaned_data['stripe_id']","                )","            except stripe.error.CardError:","                messages.error(request, \"Your card was declined!\")","            ","            if customer.paid:","                messages.error(request, \"You have successfully paid\")","                request.session['cart'] = {}","                return redirect(reverse('products'))","            else:","                messages.error(request, \"Unable to take payment\")","        else:","            print(payment_form.errors)","            messages.error(request, \"We were unable to take a payment with that card!\")","    else:","        payment_form = MakePaymentForm()","        order_form = OrderForm()","    ","    return render(request, \"checkout.html\", {\"order_form\": order_form, \"payment_form\": payment_form, \"publishable\": settings.STRIPE_PUBLISHABLE})"]}]]},"ace":{"folds":[],"scrolltop":360,"scrollleft":0,"selection":{"start":{"row":60,"column":145},"end":{"row":60,"column":145},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":24,"state":"start","mode":"ace/mode/python"}},"timestamp":1588603767881,"hash":"b29779c662f161cc01f3e9491960a73d9bea7f28"}