from flask import Flask, render_template, request
import requests
import xmltodict
import datetime

app = Flask(__name__)

def get_xml_data(data):
    # URL per ottenere i dati XML dall'endpoint /xml
    url = f'http://127.0.0.1:5000/xml?data={data}'
    response = requests.get(url)
    
    # Controlla se la richiesta ha avuto successo (status code 200)
    if response.status_code == 200:
        # Estrai i dati XML dalla risposta
        xml_data = response.text

        try:
            # Converti i dati XML in un dizionario usando xmltodict
            dati_xml = xmltodict.parse(xml_data)
            return dati_xml
        except xmltodict.ExpatError as e:
            return f"Errore durante la conversione XML: {str(e)}"
    else:
        return f"Errore durante il recupero dei dati XML: {response.status_code}"


@app.route('/', methods=['GET'])
def visualizza_dati_xml():
    # Ottieni la data selezionata dall'utente o utilizza la data corrente come default
    data_selezionata = request.args.get('data', str(datetime.date.today()))

    # Ottieni i dati XML dalla funzione get_xml_data
    dati_xml = get_xml_data(data_selezionata)

    return render_template('templateX.html', dati_xml=dati_xml, data_selezionata=data_selezionata)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
