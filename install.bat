@echo off
cls
cd C:\OpenServer\domains
git config --global user.name "Имя пользователя"
git config --global user.email "почта"
cd existing_folder
git pull
pause