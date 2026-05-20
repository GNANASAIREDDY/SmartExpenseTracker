import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from expenses.models import Expense
from income.models import Income


@login_required
def dashboard(request):

    expenses = Expense.objects.filter(user=request.user)

    total_expenses = expenses.aggregate(
        Sum('amount')
    )['amount__sum'] or 0

    transaction_count = expenses.count()

    average_expense = 0

    if transaction_count > 0:
        average_expense = total_expenses / transaction_count

    total_income = Income.objects.filter(
        user=request.user
    ).aggregate(
        Sum('amount')
    )['amount__sum'] or 0

    savings = total_income - total_expenses

    category_totals = {}

    for expense in expenses:

        category = expense.category

        if category in category_totals:
            category_totals[category] += float(expense.amount)

        else:
            category_totals[category] = float(expense.amount)

    highest_category = "No Expenses"

    if category_totals:
        highest_category = max(
            category_totals,
            key=category_totals.get
        )

    labels = list(category_totals.keys())

    data = list(category_totals.values())

    recent_expenses = expenses.order_by('-date')[:5]

    context = {
        'total_expenses': total_expenses,
        'transaction_count': transaction_count,
        'average_expense': average_expense,
        'highest_category': highest_category,
        'labels': json.dumps(labels),
        'data': json.dumps(data),
        'recent_expenses': recent_expenses,
        'total_income': total_income,
        'savings': savings,
    }

    return render(
        request,
        'analytics/dashboard.html',
        context
    )