from cProfile import label
from flask import Flask , request
from flask_cors import CORS
from flask import jsonify
from joblib import  load


# Create flask & cors instance 
app = Flask(__name__)
cors = CORS()

cors.init_app(app)

#Load Random forest classifier 
clf = load('model.joblib')

locations=[]

# Serve ESP 8266 Get request with RSSI(received signal strength indicator).
@app.route('/data', methods=['GET'])
def home():
  #Get query parameters 
  args = request.args
  data= args.to_dict()
  #Get location from model prediction
  label=clf.predict([[data.get("STUDBME1"),data.get("STUDBME2"),data.get("iot"),data.get("YME"),data.get("Miran"),data.get("CMP_LAB4"),data.get("CMP_LAB2")]])

  locations.append(label[0])
  return jsonify(label=label[0])
    
# Serve Get Request from React Server 
@app.route("/mapping", methods=['GET'])
def show_mapping():
  #Respone with the location chip exist in 
    return jsonify(label=locations[-1])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 8090,debug=True)
    	
