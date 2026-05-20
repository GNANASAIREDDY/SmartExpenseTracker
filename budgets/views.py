from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Budget
from .forms import BudgetForm


@login_required
def budget_list(request):

    budgets = Budget.objects.filter(
        user=request.user
    )

    context = {
        'budgets': budgets
    }

    return render(
        request,
        'budgets/budget_list.html',
        context
    )


@login_required
def add_budget(request):

    if request.method == 'POST':

        form = BudgetForm(request.POST)

        if form.is_valid():

            budget = form.save(commit=False)

            budget.user = request.user

            budget.save()

            return redirect('/budgets/')

    else:

        form = BudgetForm()

    context = {
        'form': form
    }

    return render(
        request,
        'budgets/add_budget.html',
        context
    )


@login_required
def edit_budget(request, pk):

    budget = get_object_or_404(
        Budget,
        pk=pk,
        user=request.user
    )

    if request.method == 'POST':

        form = BudgetForm(
            request.POST,
            instance=budget
        )

        if form.is_valid():

            form.save()

            return redirect('/budgets/')

    else:

        form = BudgetForm(instance=budget)

    context = {
        'form': form
    }

    return render(
        request,
        'budgets/add_budget.html',
        context
    )


@login_required
def delete_budget(request, pk):

    budget = get_object_or_404(
        Budget,
        pk=pk,
        user=request.user
    )

    budget.delete()

    return redirect('/budgets/')