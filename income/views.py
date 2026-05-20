from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Income
from .forms import IncomeForm


@login_required
def income_list(request):

    incomes = Income.objects.filter(
        user=request.user
    ).order_by('-date')

    context = {
        'incomes': incomes
    }

    return render(
        request,
        'income/income_list.html',
        context
    )


@login_required
def add_income(request):

    if request.method == 'POST':

        form = IncomeForm(request.POST)

        if form.is_valid():

            income = form.save(commit=False)
            income.user = request.user
            income.save()

            return redirect('income_list')

    else:
        form = IncomeForm()

    context = {
        'form': form
    }

    return render(
        request,
        'income/add_income.html',
        context
    )


@login_required
def edit_income(request, pk):

    income = get_object_or_404(
        Income,
        pk=pk,
        user=request.user
    )

    if request.method == 'POST':

        form = IncomeForm(
            request.POST,
            instance=income
        )

        if form.is_valid():
            form.save()
            return redirect('income_list')

    else:
        form = IncomeForm(instance=income)

    context = {
        'form': form
    }

    return render(
        request,
        'income/edit_income.html',
        context
    )


@login_required
def delete_income(request, pk):

    income = get_object_or_404(
        Income,
        pk=pk,
        user=request.user
    )

    income.delete()

    return redirect('income_list')