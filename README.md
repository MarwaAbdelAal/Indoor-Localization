## A WiFi tracking module using ESP8266 MCU which the user can use to localize and track the current location through either a mobile application or a website.

## Features:
- The user can visualize a basic map for the location and see a flashing point moving on the map
representing the tracked moving object.
- The user can replay the motion of the object during the last time period (corresponding to like
50 time point).

# requirements for Create flask APP

## 1- Create virtual Enviironment 

```
pip install virtualenv
virtualenv venv  
```

#### PS Don't forget to activate your virtual environment

#### In case working with windows activation may fail so check next link

[Activation](https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows)

## 2- Run main.py to run server 

> install requirements first : 
> ```
> python -m pip install -r requirements.txt
> ```

```
python main.py
```
## 3- Make sure to be in reactapp directory and run following commands for the webapp

```
npm install
npm start
```

## 4- For the mobile application make sure to be in reactnative-app directory and run following commands

```
npm install
npm start
```

## Testing APIS
1- visit http://localhost:8090/mapping to see location predicted from Random Forest Classifier

2- visit http://localhost:8090/data?STUDBME1="RSSI_Value"&STUDBME2="RSSI_Value"&RehabLab="RSSI_Value"&CMP_LAB1="RSSI_Value"&CMP_LAB2="RSSI_Value"&CMP_LAB3="RSSI_Value"&CMP_LAB4="RSSI_Value"&Dalia_iphone="RSSI_Value"&Dalialab="RSSI_Value"&Mikasa="RSSI_Value"&Nada="RSSI_Value"&YME="RSSI_Value"   to see location predicted from Random Forest Classifier

> Snapshot of the mobile application
> ![mobile_applaction_map](images/map.jpeg)