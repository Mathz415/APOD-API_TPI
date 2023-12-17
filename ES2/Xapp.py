from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def visualizza_dati_xml():
    # Sostituisci l'URL con l'URL effettivo del tuo primo server Flask
    url_dati_xml = 'http://127.0.0.1:5000/'

    try:
        # Effettua una richiesta GET per ottenere i dati XML dal primo server Flask
        response = requests.get(url_dati_xml)
        response.raise_for_status()  # Lancia un'eccezione per errori HTTP

        # Estrai i dati XML dalla risposta
        dati_xml = response.text
        return render_template('template.html', dati_xml=dati_xml)

    except requests.exceptions.HTTPError as errh:
        return {"errore": f"Errore HTTP: {errh}"}
    except requests.exceptions.ConnectionError as errc:
        return {"errore": f"Errore di connessione: {errc}"}
    except requests.exceptions.Timeout as errt:
        return {"errore": f"Timeout della richiesta: {errt}"}
    except requests.exceptions.RequestException as err:
        return {"errore": f"Errore durante la richiesta: {err}"}

if __name__ == '__main__':
    app.run(debug=True)
