#Scripts Python - Amaury
import ctypes
MessageBox = ctypes.windll.user32.MessageBoxW
MessageBox(None, 'Teste', 'Window title', 0)