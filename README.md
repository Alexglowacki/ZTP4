# ZTP4
<!-- db connection root/passwd -->

# Struktura:
 - warstwa aplikacji - folder app/ui - odpowiedzialne za frontend
 - warstwa domenowa - plik controller.py - odpowiedzialne za logikę biznesową
 - wartswa infrastrukturalna - API wszystko w folderze /app/api, /app/models odpowiedzialne za polaczenia z baza danych
 - XD
# MVC:
 - Model - pliki database_*.py
 - Controller - plik controller.py
 - View - pliki w directory app

# Running
 - in dir `/project/app/` start the database connection: `python3 controller.py`
 - in the same dir start the desktop application: `python3 main.py`
