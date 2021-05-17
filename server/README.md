# README.md 

Flask API that retrieves and posts information to Firestore and Google Cloud Storage, as well as using OpenCV to extract image data.

## Set up

First, clone the repository into your device.

```bash
git clone https://github.com/juancarlosagreda/ticket-reader.git
```

Start with installing the python dependencies, and add the config/key files into server folder.

```bash
cd ticket-reader/sever
pip install requirements.txt
```

Startup the backend application

```bash
python app.py
```

## Endpoint definitions

- GET /netValue
- GET /listAll
- POST /add/:path_to_image

## Example responses

- GET /netValue

```json
{
    "netValue":"300"
}
```

- GET /listAll

```json
{
    "Company a": { 
        "Correo":"companya@company.com",
        "Coste":"100",
        "Fecha Lectura":"14/05/2021",
        "Fecha Ticket":"29/04/2021",
        "IVA":"21",
        "NIF":"4",
        "Nombre de Empresa":"Company A",
        "Pagina web":"companya.com",
        "Telefono":"8347983"
    },
    "Company b":{
        "Correo":"companyb@company.com",
        "Coste":"200",
        "Fecha Lectura":"13/05/2021",
        "Fecha Ticket":"10/05/2021",
        "IVA":"20",
        "NIF":"2",
        "Nombre de Empresa":"Company B",
        "Numero de Factura":"2",
        "Pagina Web":"companyb.com",
        "Telefono":"37364738999"
    }
}
```

- POST /add/:path_to_image

```json
{
    "success": True
}

OR

{
    "success": False
}
```

## Licence

- [Themesberg](https://github.com/themesberg/volt-react-dashboard)
- [MIT](https://themesberg.com/licensing#mit)