var pictureSource;   
var destinationType;  
document.addEventListener("deviceready",onDeviceReady,false);

function onDeviceReady() {
    pictureSource=navigator.camera.PictureSourceType;
    destinationType=navigator.camera.DestinationType;
}
function holla(){
    responsiveVoice.speak("hello world");
}

function onPhotoDataSuccess(imageData) {
      
    //smallImage.src = "data:image/jpg;charset=UTF-8;base64," + imageData;
    console.log(imageData);
    var arr={"img_data":imageData};
    console.log(arr);
    
    //ajax here
    var http = new XMLHttpRequest();
    var url = 'https://python-mahi100.c9users.io/uploader';
    var arr={"img_data":imageData};
    arr=JSON.stringify(arr,null,'\t');
    http.open('POST', url, true);

    //Send the proper header information along with the request
    http.setRequestHeader('Content-type', 'application/json;charset=UTF-8');
    var here=0;
    http.onreadystatechange = function(){
        
        if(http.readyState == 4 && http.status == 200) {
        var obj=JSON.parse(http.responseText);
            console.log(obj);
        responsiveVoice.speak(obj.description.captions[0].text);
        }
    }

    http.send(arr);
}

function capturePhotoWithData() {
    navigator.camera.getPicture(onPhotoDataSuccess, onFail,{ quality: 50,destinationType: Camera.DestinationType.DATA_URL});
}

function onFail(message) {
    alert('Failed because: ' + message);
}


function checkConnection() {
    var networkState = navigator.connection.type;

    var states = {};
    states[Connection.UNKNOWN]  = 'Unknown connection';
    states[Connection.ETHERNET] = 'Ethernet connection';
    states[Connection.WIFI]     = 'WiFi connection';
    states[Connection.CELL_2G]  = 'Cell 2G connection';
    states[Connection.CELL_3G]  = 'Cell 3G connection';
    states[Connection.CELL_4G]  = 'Cell 4G connection';
    states[Connection.CELL]     = 'Cell generic connection';
    states[Connection.NONE]     = 'No network connection';

    alert('Connection type: ' + states[networkState]);
}



