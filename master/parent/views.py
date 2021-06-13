import json

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView

from master.models import Parent
from sample.forms import ParentForm


class ParentView(View):
    template_name='master/parent/parent_list.html'
    paginate_by = 2 

    def parent_edit(request, target_id=None):
        parent_list = []
        target_index = -1
        index = 0

        # 親レコード全取得
        parents = Parent.objects.all().order_by('id')

        # 親リスト作成
        for parent in parents:
            parent_node = dict();
            parent_node['id'] = parent.id
            parent_node['text'] = parent.name
            parent_node['link'] = "./" + str(parent.id)
            parent_list.append(parent_node)

            # 選択指定対象のデータ
            if (parent.id == target_id):
                target_index = index
            else:
                index += 1

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
                    return redirect('master.parent:parent_list')
                    # return redirect('sample:parent_list')
                    # return redirect('parent:parent_list_by_id', target_id = target_id)
                else:
                    return redirect('master.parent:parent_list')
        
        form = ParentForm(instance=parents[target_index])
        return render(request, 'master/parent/parent_list.html', dict(
            parent_list = json.dumps(parent_list),
            target_index = target_index,
            target_id = target_id,
            form = form
        ))
