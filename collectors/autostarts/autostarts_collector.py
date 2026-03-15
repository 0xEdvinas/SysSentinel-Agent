import subprocess
import winreg
import os

class AutostartsCollector:
    def __init__(self):
        pass
    
    def get_registry_autostarts(self):
      path = r"Software\Microsoft\Windows\CurrentVersion\Run"

      key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path)

      i = 0
      autostarts = []

      while True:
          try:
              # returns name, value, convention
              name, value, _ = winreg.EnumValue(key, i)
              autostarts.append({ 
                  'name': name, 
                  'path': value 
                 })
              
              i += 1
          except OSError:
              break

      return autostarts
    
    def get_startupfolder_autostarts(self):
        startup_folder = os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup")

        autostarts = []

        for item in os.listdir(startup_folder):
            item_path = os.path.join(startup_folder, item)
            if os.path.isfile(item_path):
                autostarts.append({ 
                      'name': item, 
                      'path': item_path 
                     }
                )

        return autostarts
    
    def get_scheduled_tasks_autostarts(self):
        result = subprocess.run(['schtasks', '/query', '/fo', 'LIST'], capture_output=True, text=True)
        output = result.stdout

        autostarts = []
        current_task = {}

        for line in output.splitlines():
            if line.startswith("TaskName:"):
                if current_task:
                    autostarts.append(current_task)
                    current_task = {}
                current_task['name'] = line.split(":", 1)[1].strip()
            elif line.startswith("Task To Run:"):
                current_task['path'] = line.split(":", 1)[1].strip()

        if current_task:
            autostarts.append(current_task)

        return autostarts


    
