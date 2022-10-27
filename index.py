import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

cred = credentials.Certificate("test-b3679-firebase-adminsdk-4zy4y-d1e17b0009.json")
firebase_admin.initialize_app(cred)
# Application Default credentials are automatically created.
db = firestore.client()

users_ref = db.collection(u'utenti')
docs = users_ref.stream()

doc_ref = db.collection(u'utenti').document(u'alovelace')
doc_ref.set({
    u'nome': u'Ada',
    u'cognome': u'Lovelace',
    u'anno': 1815
})


for doc in docs:
    print(doc.to_dict()['nome'])
    #print(f'{doc.id} => {doc.to_dict()}')
print('-----')

cities_ref = db.collection("utenti")
query = cities_ref.order_by("nome").limit(4)
results = query.get()
for doc in results:
    print(doc.to_dict()['nome'])