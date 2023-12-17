from flask import Flask, render_template, request
import requests
import datetime
import xmltodict

app = Flask(__name__)

def convert_to_xml(json_data):
    try:
        # Assicurati che ci sia un elemento radice chiamato "root"
        root_element = {"root": json_data}

        xml_data = xmltodict.unparse(root_element, pretty=True)
        return xml_data
    except Exception as e:
        return f"Errore durante la conversione JSON to XML: {str(e)}"



def get_data_NASA_API(data):
    # Imposta la tua chiave API NASA
    api_key = 'SV3ftunNB8SLaZuZqhrpEJnfc8yaokNvDD7bWO6e'

    # URL dell'API della NASA per l'immagine del giorno
    url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&date={data}'

    try:
        # Effettua la richiesta GET all'API della NASA
        response = requests.get(url)
        response.raise_for_status()  # Lancia un'eccezione per errori HTTP

        # Estrai i dati JSON dalla risposta
        dati_nasa = response.json()
        
        return dati_nasa
    
    except requests.exceptions.HTTPError as errh:
        return {"errore": f"Errore HTTP: {errh}"}
    except requests.exceptions.ConnectionError as errc:
        return {"errore": f"Errore di connessione: {errc}"}
    except requests.exceptions.Timeout as errt:
        return {"errore": f"Timeout della richiesta: {errt}"}
    except requests.exceptions.RequestException as err:
        return {"errore": f"Errore durante la richiesta: {err}"}

@app.route('/', methods=['GET'])
def visualizza_immagine():
    # Ottieni la data selezionata dall'utente o utilizza la data corrente come default
    data_selezionata = request.args.get('data', str(datetime.date.today()))

    # Chiama la funzione che recupera i dati dall'API NASA
    dati_nasa = get_data_NASA_API(data_selezionata)

    # Converti i dati JSON in XML
    dati_xml = convert_to_xml(dati_nasa)

    return dati_xml

if __name__ == '__main__':
    app.run(debug=True)
