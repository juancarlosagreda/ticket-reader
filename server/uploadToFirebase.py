import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('./config.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection(u'ticketreader')


def newTicket(email, cost, flectura, fticket, IVA, NIF, company, wpage, number):
    # data structure for every ticket
    ticketData = {
        u'Correo': email,
        u'Coste': cost,
        u'Fecha Lectura': flectura,
        u'Fecha Ticket': fticket,
        u'IVA': IVA,
        u'NIF': NIF,
        u'Nombre de Empresa': company,
        u'Pagina Web': wpage,
        u'Telefono': number
    }

    #all_tickets = [doc.to_dict() for doc in doc_ref.stream()]

    doc_ref.add(ticketData)

    print(ticketData)


"""
newTicket("Company D", "companyc@company.com", "40", "01/01/2021", "03/04/2020",
          "21", "ABC1234", "Company C", "companyc.com", "635112260")
"""
