import json

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView

from master.models import Parent
from master.forms import ParentForm


def master(request):
    return render(request, 'master/master_base.html')

class ParentView(View):
    def parent_edit(request, target_id=None):
        parent_list = []
        index = 0

        # 親レコード全取得
        parents = Parent.objects.all().order_by('id')

        # 親リスト作成
        for parent in parents:
            parent_node = dict();
            parent_node['id'] = parent.id
            parent_node['name'] = parent.name
            parent_node['link'] = "/master/parent/" + str(parent.id)
            parent_list.append(parent_node)

            # 編集対象のデータ
            if (parent.id == target_id):
                form = ParentForm(instance=parent)

        if request.method == 'POST':
            if target_id:
                parent = get_object_or_404(Parent, pk=target_id)
            else:
                parent = Parent()

            form = ParentForm(request.POST, instance=parent)

            if form.is_valid():
                parent = form.save(commit=False)
                parent.save()
                if target_id:
                    return redirect('master:parent_list_by_id', target_id = target_id)
                else:
                    return redirect('master:parent_list')
        
        if(target_id == None):
            form = ParentForm(instance=Parent())
        return render(request, 'master/parent_list.html', dict(
            parent_list = json.dumps(parent_list),
            target_id = target_id,
            form = form
        ))
        
    def parent_del(request, target_id):
        """親削除"""
        parent = get_object_or_404(Parent, pk=target_id)
        parent.delete()
        return redirect('master:parent_list')
