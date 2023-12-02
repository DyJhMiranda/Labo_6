from datamanager import RealTimeDataManager
import time
# Actualizaciones en tiempo real en segundo plano
import threading

def print_notifications(data):
  print("Datos en tiempo real actualizados:", data)

real_time_data_manager = RealTimeDataManager()
real_time_data_manager.event_manager.subscribe("any", print_notifications)
update_thread = threading.Thread(target=real_time_data_manager.start_real_time_updates)
update_thread.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nPrograma terminado.")

