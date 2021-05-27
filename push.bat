@echo off
cls
git add --all
git pull origin master
git push origin master
git commit -m "New changes"
git push
pause