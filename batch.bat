@echo off
set online=%1
echo %online%
md %online% %online%\classes
echo "" > .\%online%\classes\FreeUser.py
echo "" > .\%online%\classes\PaidUser.py
echo "" > .\%online%\classes\Plan.py
echo "" > .\%online%\classes\Silver.py
echo "" > .\%online%\classes\Gold.py
echo "" > .\%online%\classes\Diamond.py
echo "" > .\%online%\classes\Product.py
echo "" > .\%online%\classes\Review.py
