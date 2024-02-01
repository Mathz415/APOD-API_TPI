from flask import Flask, render_template, request
import requests
import xmltodict
import datetime

app = Flask(__name__)

# ... (resto del codice)

@app.route('/visualizza_xml', methods=['GET'])
def visualizza_dati_xml():
    url_dati_xml = 'http://127.0.0.1:5000/xml'

    try:
        response = requests.get(url_dati_xml)
        response.raise_for_status()

        dati_xml_str = response.text

        # Converti la stringa XML in un dizionario
        dati_xml_dict = xmltodict.parse(dati_xml_str)

        return render_template('templateX.html', dati_xml=dati_xml_dict)

    except requests.exceptions.HTTPError as errh:
        return {"errore": f"Errore HTTP: {errh}"}
    except requests.exceptions.ConnectionError as errc:
        return {"errore": f"Errore di connessione: {errc}"}
    except requests.exceptions.Timeout as errt:
        return {"errore": f"Timeout della richiesta: {errt}"}
    except requests.exceptions.RequestException as err:
        return {"errore": f"Errore durante la richiesta: {err}"}

# ... (resto del codice)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
