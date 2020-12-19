// Initialize Firebase
var config = {
  apiKey: "AIzaSyD8Z4lfgdsvmDYZwDGgpCr-z_cxIrYxgC8",
    authDomain: "crime-registration-bot.firebaseapp.com",
    databaseURL: "https://crime-registration-bot-default-rtdb.firebaseio.com",
    projectId: "crime-registration-bot",
    storageBucket: "crime-registration-bot.appspot.com",
    messagingSenderId: "214503224041",
    appId: "1:214503224041:web:f31cc5ed6df18c52d27678"
};
firebase.initializeApp(config);

// Reference messages collection
var messagesRef = firebase.database().ref('messages');



var fileUpload = document.getElementById("cameraInput");

  fileUpload.addEventListener('change', function(evt) {
    var firstFile = evt.target.files[0]; // upload the first file only
    var storageRef = firebase.storage().ref('photos/'+firstFile.name);
    storageRef.put(firstFile);
});



// Listen for form submit
document.getElementById('contactForm').addEventListener('submit', submitForm);

// Submit form
function submitForm(e){
  e.preventDefault();

  //Get value
  var fname = getInputVal('fname');
  var lname = getInputVal('lname');
  var email = getInputVal('email');
  var phone = getInputVal('phone');
  var street = getInputVal('street');
  var address = getInputVal('address');
  var city = getInputVal('city');
  var state = getInputVal('state');
  var country = getInputVal('country');
  var pincode = getInputVal('pincode');
  


  var complaint = getInputVal('complaint');

  // Save message
  saveMessage(fname, lname, email, phone, street, address, city, state, country, pincode, complaint);

  

  // Show alert
  document.querySelector('.alert').style.display = 'block';

  // Hide alert after 3 seconds
  setTimeout(function(){
    document.querySelector('.alert').style.display = 'none';
  },3000);

  // Clear form
  document.getElementById('contactForm').reset();
}

// Function to get form value
function getInputVal(id){
  return document.getElementById(id).value;
}






// Save message to firebase
function saveMessage(fname, lname, email, phone, street, address, city, state, country, pincode, complaint){
  var newMessageRef = messagesRef.push();
  newMessageRef.set({
    fname: fname,
    lname: lname,
    email: email,
    phone: phone,
    street:street,
    address:address,
    city:city,
    state:state,
    country:country,
    pincode:pincode,
    complaint: complaint
  });
}
