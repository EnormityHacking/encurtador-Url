import pyshorteners

print ()
print ("  \033[1;32m")
print("• ENCURTADOR DE URLS •")
print ("• Desenvolvido Por Zeus Xaloc •")
print()
url = 'https://www.instagram.com/enormityhacking_org'

s = pyshorteners.Shortener()

shortUrl = s.tinyurl.short(url)

print(f"URL Encurtada: {shortUrl}")
print()
print("URL  Encurtada Com Sucesso!")