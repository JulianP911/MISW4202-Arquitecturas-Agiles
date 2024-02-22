import logging

def setup_logger():
    logging.basicConfig(filename='monitor_notifificaciones.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger()
