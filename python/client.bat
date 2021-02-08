@echo off

::server
::call \\tsclient\G\python-3.8.5-embed-amd64\python \\tsclient\G\study\learn\myproject\app.py
::call \\tsclient\F:\RDA8955\Code\GM5\WH-GM5\prebuilts\win32\python3\python \\tsclient\\\tsclient\G\study\learn\myproject\selftest\python\threading_socket.py

::local
::call %CSDTK4INSTALLDIR%\..\..\..\Python37\python app.py
call python circle_tcp_client.py


pause