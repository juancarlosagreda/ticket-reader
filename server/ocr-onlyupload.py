import os
import io
from google.cloud import vision
from google.cloud import storage
import cv2 as cv
import json
import re
from datetime import date

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = fr"./APIKeyPython.json"

# Funcion de Google para extaer texto(solo funciona con path, no parsed hasta donde yo se)


def detect_text(path):
    '''
    Detecta el texto usando el API de Google Vision. Queremos minimizar el uso de este API para reducir costes,
    solo se aplica en casos en los cuales el OCR Tesseract detecta un texto mínimo primero (Variable definida en base a pruebas).

    Este API requiere conexión a internet y se ha demostrado que lo mas lento de su aplicacion es la subida de imágenes al internet.
    Dependiente de la calidad de la imagen que se utiliza. 
    '''
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)

    if response.error.message:
        # Regresa el tipo de error que sucede de acuerdo a lo definido por Google
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    return response

# Funcion para subir a google cloud storage


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

# Funciones en regex para buscar infomracion utilizando regex


def encontrarfechas(data):
    # Este RegEx sirve para detectar las fechas en formato AÑO/MES/DÍA o DÍA/MES/AÑO
    today = date.today()
    today = today.strftime("%Y%m%d")
    today.join(today)
    # Este RegEx sirve para detectar las fechas en formato AÑO/MES/DÍA o DÍA/MES/AÑO
    b = r"(?:Factura.*|FACTURA|factura|Emis.*|firma|Fecha|FECHA|cargo.*|expedición)? ?:?\n?\n?\n?.*?\n?.*?\n?(?:(\d{2})(?:[\/\- \.]| de )([0-3][0-9]|ene|feb|mar|abr|may|jun|jul|ago|sep|sept|oct|nov|dic|enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)(?:[\/\- \.]| de )(\d{2,4}))\n"
    c = re.findall(b, data)
    d = "Null"
    # En algunos casos, se guardan fechas posteriores. Por tanto, se descarta toda fecha posterior a la primera
    if len(c):
        d = c[0]

    # Con este algoritmo se convierten las fechas a formato uniforme
    if len(d) == 3:
        if len(d[2]) == 2:
            if d[1] == "ene" or d[1] == "enero":
                e = "20"+d[2]+"01"+d[0]
            elif d[1] == "feb" or d[1] == "febrero":
                e = "20"+d[2]+"02"+d[0]
            elif d[1] == "mar" or d[1] == "marzo":
                e = "20"+d[2]+"03"+d[0]
            elif d[1] == "abr" or d[1] == "abril":
                e = "20"+d[2]+"04"+d[0]
            elif d[1] == "may" or d[1] == "mayo":
                e = "20"+d[2]+"05"+d[0]
            elif d[1] == "jun" or d[1] == "junio":
                e = "20"+d[2]+"06"+d[0]
            elif d[1] == "jul" or d[1] == "julio":
                e = "20"+d[2]+"07"+d[0]
            elif d[1] == "ago" or d[1] == "agosto":
                e = "20"+d[2]+"08"+d[0]
            elif d[1] == "sep" or d[1] == "sept" or d[1] == "septiembre":
                e = "20"+d[2]+"09"+d[0]
            elif d[1] == "oct" or d[1] == "octubre":
                e = "20"+d[2]+"10"+d[0]
            elif d[1] == "nov" or d[1] == "noviembre":
                e = "20"+d[2]+"11"+d[0]
            elif d[1] == "dic" or d[1] == "diciembre":
                e = "20"+d[2]+"12"+d[0]
            else:
                e = "20"+d[2]+d[1]+d[0]
        else:
            if d[1] == "ene" or d[1] == "enero":
                e = d[2]+"01"+d[0]
            elif d[1] == "feb" or d[1] == "febrero":
                e = d[2]+"02"+d[0]
            elif d[1] == "mar" or d[1] == "marzo":
                e = d[2]+"03"+d[0]
            elif d[1] == "abr" or d[1] == "abril":
                e = d[2]+"04"+d[0]
            elif d[1] == "may" or d[1] == "mayo":
                e = d[2]+"05"+d[0]
            elif d[1] == "jun" or d[1] == "junio":
                e = d[2]+"06"+d[0]
            elif d[1] == "jul" or d[1] == "julio":
                e = d[2]+"07"+d[0]
            elif d[1] == "ago" or d[1] == "agosto":
                e = d[2]+"08"+d[0]
            elif d[1] == "sep" or d[1] == "sept" or d[1] == "septiembre":
                e = d[2]+"09"+d[0]
            elif d[1] == "oct" or d[1] == "octubre":
                e = d[2]+"10"+d[0]
            elif d[1] == "nov" or d[1] == "noviembre":
                e = d[2]+"11"+d[0]
            elif d[1] == "dic" or d[1] == "diciembre":
                e = d[2]+"12"+d[0]
            else:
                e = d[2]+d[1]+d[0]
    else:
        e = d
    if int(e) > int(today):
        e = "Null"
    return e


def encontrarnomempresa(data):
    a = r"(?:([A-ZÁÉÍÓÚÑ ]*\.?,? S\.(?:L|A)\.)|([A-ZÁÉÍÓÚÑ ]?[a-záéíóúñ]*\.?,? S\.(?:L|A)\.)|(?:(?:www\.)?([a-zA-Z0-9!#$%&'*\+\-\/=?^_`{|}~]*)\.(?:com|es)))"
    b = re.findall(a, data)
    if len(b):
        b = b[0]
        if b[0]:
            b = b[0].upper()
        elif b[1]:
            b = b[1].upper()
        elif b[2]:
            b = b[2].upper()
    else:
        b = "Null"
    return b


def encontrarNIF(data):
    a = r"([A-J][- ]?\d{8,10}|\d{8,10}[- ]?[A-J])[\n ]"
    b = re.findall(a, data)
    # En algunos casos, se guardan NIFs de clientes. Por tanto, se descarta toda fecha posterior a la primera
    if len(b):
        b = b[0]
    else:
        b = "Null"
    # Con este algoritmo se estandarizan a formato uniforme
    if re.findall(r"[A-J]", b[0]):
        if re.findall(r"[- ]", b[1]):
            b = b[0]+b[2:]
    elif re.findall(r"[A-J]", b[len(b)-1]):
        if re.findall(r"[- ]", b[len(b)-2]):
            b = b[len(b)]+b[:(len(b)-3)]
        else:
            b = b[len(b)-1]+b[:(len(b)-1)]
    return b


def encontrarnumfactura(data):
    a = r"(?:(?:Numero:|Factura:|factura|N° fra\.simp:|N° FACTURA:) ?\n?([A-Z\d \-\/]*)\n|(?:Numero:|Factura:|factura|FACTURA|N° fra\.simp:)\n([\d{1,4} ]*)\n)"
    b = re.findall(a, data)
    if len(b):
        b = b[0]
        if b[0]:
            b = b[0]
        elif b[1]:
            b = b[1]
        else:
            b = "Null"
    else:
        b = "Null"
    return b


def encontrarIVA(data):
    VA = list()
    a = r"(?:IVA|I.V.A.)?[: \n]?(21|16|10|4)[.,]?0?0? ?%"
    b = r"\n(21|16|10|4)\n"
    c = list(r+"%" for r in re.findall(a, data)) + \
        list(s+"%" for s in re.findall(b, data))
    d = ""
    if not len(c):
        d = "Null"
    else:
        if "4%" in c:
            d = "4% "
        if "10%" in c:
            d = d+"10% "
        if "16%" in c:
            d = d+"16%"
        if "21%" in c:
            d = d+"21%"
    return d


def encontrarcoste(data):
    a = r"(?:TOTAL|Total|Líquido)[:\w\s]*\n([\d{3}]?[.,]?\d{2,6}[.,]\d{2})"
    b = re.findall(a, data)
    if not len(b):
        c = r"(?:TOTAL|Total|Líquido)[:\w\s]*\n(\d{1,3}?[.,]?\d{2,6}[.,]\d{2})"
        b = re.findall(c, data)
        if not len(b):
            d = r"(?:TOTAL|Total)[:\w\s]*\n(?:Importe en euros:?\n)?([\d{3}]?[.,]?\d{1,6}[.,]\d{2})"
            b = re.findall(d, data)
            if not len(b):
                e = r"(\d{1,3}?[.,]?\d{1,6}[.,]\d{2})€?\n"
                b = re.findall(e, data)
    if len(b):
        for i in range(len(b)):
            x = list(b[i])
            if "." in x:
                x.remove(".")
            if "," in x:
                x.remove(",")
            d = ""
            b[i] = int(d.join(x))
        b = max(b)
        y = list(str(b))
        y.insert(len(y)-2, ".")
        z = ""
        b = z.join(y)
    else:
        b = "Null"
    if not (b == "Null"):
        b = b+" €"
    return b


def encontrartelefono(data):
    a = r"(?:\n(?:\+34)? ?([9,6]\d{8})\n|(?:TEL|Teléfono)[:\. \n]*(\d{2,3} ?\d{2,3} ?\d{2} ?\d{2}|\d*)|(\d{3}[\. -]\d{3}[\. -]\d{3})|([69]\d{2} ?\d{2} ?\d{2} ?\d{2}))"
    b = re.findall(a, data)
    if len(b):
        if len(b[0][0]):
            b = b[0][0]
        elif len(b[0][1]):
            b = b[0][1]
        elif len(b[0][2]):
            b = b[0][2]
        elif len(b[0][3]):
            b = b[0][3]
        else:
            b = "Null"
    else:
        b = "Null"
    c = list(b)
    for d in c:
        if d == " ":
            c.remove(" ")
    d = ""
    b = d.join(c)
    return b


def encontrarcorreo(data):
    a = r"([a-zA-Z0-9!#$%&'*+-\/=?^_`{|}~]*@[a-zA-Z0-9!#$%&'*+\/=?^_`{|}~\.]*\.(?:com|es))"
    b = re.findall(a, data)
    if len(b):
        b = b[0]
    else:
        b = "Null"
    return b


def encontrarpaginaweb(data):
    a = r"(?:www\.)?([a-zA-Z0-9!#$%&'*\+\-\/=?^_`{|}~]*\.(?:com|es))"
    b = re.findall(a, data)
    if len(b):
        b = b[0]
    else:
        b = "Null"
    return b


def fechadelectura():
    today = date.today()
    today = today.strftime("%Y%m%d")
    today.join(today)
    return today

# Funcion para extaer toda la informacion


def extraerinformacion(path):
    response = detect_text(path)
    data = response.text_annotations[0].description
    informacion = {
        'fechadelectura': fechadelectura(),
        'fechas': encontrarfechas(data),
        'nomempresa': encontrarnomempresa(data),
        'NIF': encontrarNIF(data),
        'numfactura': encontrarnumfactura(data),
        'IVA': encontrarIVA(data),
        'coste': encontrarcoste(data),
        'telefono': encontrartelefono(data),
        'correo': encontrarcorreo(data),
        'paginaweb': encontrarpaginaweb(data)
    }
    return informacion


r'''
        dictionary={f"{file.split('.')[0]}":response.text_annotations[0].description}
            data=json.load(outfile)
            data.update(dictionary)
            outfile.seek(0)
            json.dump(data, outfile,indent=4,sort_keys=True)
            

            data=json.load(outfile)
            outfile.seek(0)
            data[f"{file.split('.')[0]}"]=response.text_annotations[0].description
            outfile.write(json.dumps(data,indent=4,sort_keys=True))
'''

if __name__ == "__main__":
    extraerinformacion(
        './Imagenes/ticket.jpg')
