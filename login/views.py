from django.con.auth import login as auth_logon
from django.shortcuts import render, redirect
from django.urls import revers
from django.views import View

from .forms import LoginForm


class LoginView(View):
    def get(self, request, *args, **kwargs):
        """GETリクエスト用のメソッド"""
        context = {
            'from' : LoginForm(),
        }
        # ログイン画面用のテンプレートの値がからのフォームをレタリング
        return render(request, login/login.html, context)
        