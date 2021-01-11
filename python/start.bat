@echo off

::直接在远程桌面上运行
::call \\tsclient\G\python-3.8.5-embed-amd64\python \\tsclient\G\study\learn\myproject\app.py
::call \\tsclient\G\Python37\python \\tsclient\G\study\learn\myproject\phn\main_test.py

::在本地执行
::call %CSDTK4INSTALLDIR%\..\..\..\Python37\python app.py
call python qipan.py



pause