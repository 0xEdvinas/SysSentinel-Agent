import winreg

class AutostartsCollector:
    def __init__(self):
        pass
    
    def get_registry_autostarts(self):
      path = r"Software\Microsoft\Windows\CurrentVersion\Run"

      key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path)

      i = 0
      programs = []

      while True:
          try:
              name, value, _ = winreg.EnumValue(key, i)
              programs.append((name, value))
              i += 1
          except OSError:
              break

      return programs
    
    
    
