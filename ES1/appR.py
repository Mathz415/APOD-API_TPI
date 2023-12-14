from flask import Flask, render_template, request
import requests
import datetime

app = Flask(__name__)


def get_data_NASA_API(data_inziale, data_finale):
    # Imposta la tua chiave API NASA
    api_key = 'SV3ftunNB8SLaZuZqhrpEJnfc8yaokNvDD7bWO6e'

    # URL dell'API della NASA per l'immagine del giorno
    url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&start_date={data_inziale}&end_date={data_finale}'

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

@app.route('/', methods=['POST','GET'])
def visualizza_immagine():
    # Ottieni la data selezionata dall'utente o utilizza la data corrente come default
    data_inziale = request.args.get('data-iniziale', str(datetime.date.today()))
    data_finale = request.args.get('data-finale', str(datetime.date.today()))

    # Chiama la funzione che recupera i dati dall'API NASA
    dati_nasa = get_data_NASA_API(data_inziale, data_finale)

    return render_template('templateR.html', dati_nasa=dati_nasa, data_inziale=data_inziale, data_finale=data_finale)

if __name__ == '__main__':
    app.run(debug=True)
