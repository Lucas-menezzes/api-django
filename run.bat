@echo off

rem Este script inicia o servidor e executa os testes automaticamente

rem Inicia o servidor em segundo plano
start "Django Server" python manage.py runserver

rem Aguarda alguns segundos para garantir que o servidor tenha iniciado
timeout /t 5 /nobreak

rem Executa os testes
python manage.py test films.tests.first_tests