import json

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic import RedirectView

from sample.models import Parent
from sample.forms import ParentForm


class ParentListView(ListView):
    template_name='sample/parent_list.html'
    context_object_name='parents'
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        """親一覧"""
        parents = Parent.objects.all().order_by('id')
        self.object_list =parents
        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)

class ParentView(View):
    def parent_edit(request, parent_id=None):
        """親編集"""
        if parent_id:
            parent = get_object_or_404(Parent, pk=parent_id)
        else:
            parent = Parent()

        if request.method == 'POST':
            form = ParentForm(request.POST, instance=parent)
            if form.is_valid():
                parent = form.save(commit=False)
                parent.save()
                return redirect('sample:parent_list')
        else:
            form = ParentForm(instance=parent)

        return render(request, 'sample/parent_edit.html', dict(form=form, parent_id=parent_id))
    
    def parent_del(request, parent_id):
        """親削除"""
        parent = get_object_or_404(Parent, pk=parent_id)
        parent.delete()
        return redirect('sample:parent_list')


class ChildListView(ListView):
    """子一覧"""
    template_name='sample/child_list.html'
    context_object_name='children'
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        parent = get_object_or_404(Parent, pk=kwargs['parent_id'])
        children = parent.children.all().order_by('id')
        self.object_list = children
        context = self.get_context_data(object_list=self.object_list, parent=parent)
        return self.render_to_response(context)


class NavigationView(View):
    """ナビゲーション"""
    template_name='sample/navigation.html'

    def get(self, request, *args, **kwargs):
        navigation = [];
        
        parents = Parent.objects.all().order_by('id')
        for parent in parents:
            parent_node = dict();
            parent_node['text'] = parent.name
            parent_node['nodes'] = []
            navigation.append(parent_node)

            children = parent.children.all().order_by('id')
            for child in children:
                child_node = dict();
                child_node['text'] = child.name
                child_node['nodes'] = []
                parent_node['nodes'].append(child_node)
        return render(request, self.template_name, {'navigation': json.dumps(navigation)})
        

class NavigationView2(View):
    """ナビゲーション"""
    template_name='sample/navigation2.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
