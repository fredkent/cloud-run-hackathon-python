
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging
import random
import json
from flask import Flask, request

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'T', 'L', 'R']

@app.route("/", methods=['GET'])
def index():
    return "Let the battle begin!"

@app.route("/", methods=['POST'])
def move():
    request.get_data()
    #logger.info(request.json)
    tmp=json.dumps(request.json)
    j=json.loads(tmp)
    #target=j.find("http://127.0.0.1:8080")
    myState=j["arena"]["state"]["https://cloud-run-hackathon-python-l7bu23fjpq-de.a.run.app"]
    myPositionX=myState["x"]
    myPositionY=myState["y"]
    myDirection=myState["direction"]
    myHit=myState["wasHit"]
    print(myState,myPositionX,myPositionY)
    if myHit == True:
        print("動作" + moves[0])
        return moves[0]
    #return moves[random.randrange(0)]
    else:
        randomMove=random.randrange(1,4)
        print("動作" + moves[randomMove])
        return moves[randomMove]

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
