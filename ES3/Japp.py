from flask import Flask, render_template, request
import requests
import xmltodict
import datetime

app = Flask(__name__)

def get_json_data(data):
    # URL per ottenere i dati JSON dall'endpoint /json
    url = f'http://127.0.0.1:5000/json?data={data}'
    
    try:
        # Effettua la richiesta GET all'endpoint /json
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
def visualizza_dati_json():
    # Ottieni la data selezionata dall'utente o utilizza la data corrente come default
    data_selezionata = request.args.get('data', str(datetime.date.today()))

    # funzione che recupera i dati JSON dall'endpoint /json
    dati_nasa = get_json_data(data_selezionata)

    return render_template('template.html', dati_nasa=dati_nasa, data_selezionata=data_selezionata)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
