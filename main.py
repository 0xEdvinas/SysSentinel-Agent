import collectors.autostarts.autostarts_collector as autostarts_collector

def main():
   collector = autostarts_collector.AutostartsCollector()

   autostarts = collector.get_windows_services_autostarts()

   for autostart in autostarts:
      print(f"Name: {autostart['name']}, Path: {autostart.get('path', 'N/A')}")

if __name__ == "__main__":    
   main()