# Fichier app.py pour le Nester

from flask import Flask, render_template
import os
import xml.etree.ElementTree as ET

app = Flask(__name__)

# Fonction pour obtenir la liste des fichiers XML des Harvesters
def get_harvesters_list():
    script_path = os.path.dirname(os.path.abspath(__file__))  # Chemin du répertoire du script
    harvester_path = os.path.join(script_path, 'path_to_xml_files')  # Assurez-vous d'avoir le bon chemin
    return [f.split('.')[0] for f in os.listdir(harvester_path) if f.endswith('.xml')]

# Fonction pour extraire les informations du fichier XML
def extract_info_from_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    ip_address = root.find('ip_address').text.strip()
    connected_machines = int(root.find('connected_machines').text.strip())
    
    last_scan_timestamp = root.find('last_scan/timestamp').text.strip()
    
    results = []
    for machine_elem in root.findall('last_scan/results/machine'):
        machine = {
            'name': machine_elem.find('name').text.strip(),
            'ip': machine_elem.find('ip').text.strip(),
            'open_ports': [port.text.strip() for port in machine_elem.findall('open_ports/port')]
        }
        results.append(machine)

    wan_latency = root.find('wan_latency').text.strip()

    return {
        'ip_address': ip_address,
        'connected_machines': connected_machines,
        'last_scan_timestamp': last_scan_timestamp,
        'results': results,
        'wan_latency': wan_latency
    }

# Route pour afficher la liste des Harvesters
@app.route('/')
def index():
    harvester_list = get_harvesters_list()
    return render_template('index.html', harvester_list=harvester_list)

# Route pour afficher les informations d'un Harvester
@app.route('/harvester/<harvester_id>')
def harvester_dashboard(harvester_id):
    script_path = os.path.dirname(os.path.abspath(__file__))  # Chemin du répertoire du script
    harvester_file = os.path.join(script_path, 'path_to_xml_files', f'{harvester_id}.xml')  # Assurez-vous d'avoir le bon chemin
    
    # Vérifiez si le fichier XML existe
    if not os.path.isfile(harvester_file):
        return f"Le fichier XML pour le Harvester {harvester_id} n'existe pas."

    harvester_info = extract_info_from_xml(harvester_file)
    
    # Vérifiez si harvester_info est défini
    if not harvester_info:
        return f"Impossible de récupérer les informations du Harvester {harvester_id}."

    return render_template('harvester_dashboard.html', harvester_id=harvester_id, harvester_info=harvester_info)

if __name__ == '__main__':
    app.run(debug=True)
