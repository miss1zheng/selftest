call F:\RDA8955\Code\2G\CSDTK4.2\CSDTKvars.bat
set PATH=D:\CSDTK\cygwin\bin;%PATH%
set "year=%date:~2,2%"
set "month=%date:~5,2%"
set "day=%date:~8,2%"
set "hour=%time:~0,2%"
set "min=%time:~3,2%"
set "sec=%time:~6,2%"
set USER_PRODUCT=%year%/%month%/%day%,%hour%:%min%:%sec%

@echo %USER_PRODUCT%

make

::make clean

Pause