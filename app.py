#
# oStore
# by gdRipoll
#
from flask import Flask, request
import json

from ostore.ostore import OStore

app = Flask(__name__)


# # UPSERT creación/reemplazo de una key
# [POST] http://host/version/service[?ttl=timetolive]
# {
# 	JSON Body
# }
#
# # recuperación de una key
# [GET] http://host/version/service/{hash}
#
# # eliminacion de una key
# [DELETE] http://host/version/service/{hash}


@app.route("/<string:collection>/<string:hash_id>", methods=['GET'])
def load(collection, hash_id):
    os = OStore()
    vuelta = os.load(collection, hash_id)
    print("%s >> %s" % (collection, hash_id))
    print(vuelta)
    # vuelta['_id'] = str(vuelta['_id'])
    # return json.dumps(vuelta)
    return "algo"


@app.route("/<string:collection>", methods=['POST'])
def save(collection):
    dato = request.get_json()
    os = OStore()
    my_hash = os.save(collection, dato)
    print(my_hash)
    vuelta = os.load(collection, my_hash)
    vuelta['_id'] = str(vuelta['_id'])
    print(vuelta)
    return json.dumps(vuelta)


@app.route("/", methods=['GET'])
def about():
    return json.dumps({
        "OStore": "v0.0.00"
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0")
