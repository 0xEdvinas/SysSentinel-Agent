import collectors.autostarts.autostarts_collector as autostarts_collector

def main():
   collector = autostarts_collector.AutostartsCollector()

   autostarts = collector.get_registry_autostarts()

   for autostart in autostarts:
      print(f"Name: {autostart[0]}, Path: {autostart[1]}")

if __name__ == "__main__":    
   main()