@echo off
echo Downloading python
curl -o python.exe https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe
echo installing python,  please allow installer!!
python.exe /quiet InstallAllUsers=1 PrependPath=1