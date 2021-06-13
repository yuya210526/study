import datetime
import json

from django.db.models import F, Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView

from master.models import Parent
from plan.models import Plan
from plan.forms import PlanForm

class PlanView(View):
    def plan_edit(request, target_date, target_category, target_id):
        navigation = []
        plan_id = None
        
        parents = Parent.objects.all().order_by('id')
        for parent in parents:
            parent_node = dict()
            parent_node['category'] = Plan.PALENT
            parent_node['id'] = parent.id
            parent_node['name'] = parent.name
            parent_node['children'] = []
            navigation.append(parent_node)

            children = parent.children.all().order_by('id')
            for child in children:
                child_node = dict()
                child_node['category'] = Plan.CHILD
                child_node['id'] = child.id
                child_node['name'] = child.name
                child_node['children'] = []
                parent_node['children'].append(child_node)

        # 計画取得
        # https://qiita.com/uenosy/items/54136aff0f6373957d22
        # https://yaruki-strong-zero.hatenablog.jp/entry/django_model_lookup
        t_target_datetime = datetime.datetime.strptime(target_date, '%Y-%m-%d')
        t_target_date = datetime.date(t_target_datetime.year, t_target_datetime.month, t_target_datetime.day)
        plans = Plan.objects.filter(Q(target_category=target_category) & Q(target_id=target_id) & Q(target_date=t_target_date))
        if(plans.count()):
            plan_id = plans[0].id
            form = PlanForm(instance=plans[0])
        else:
            form = PlanForm(instance=Plan())

        return render(request, 'plan/navigation.html', dict(
            navigation = json.dumps(navigation),
            target_date = target_date,
            target_category = target_category,
            target_id = target_id,
            plan_id = plan_id,
            form = form
        ))
