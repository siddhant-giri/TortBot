 var firebaseConfig = {
    apiKey: "AIzaSyAiwgQFJpEx_QTzNNWY8FD3iYjsZsxbzgQ",
    authDomain: "tortbot-admin.firebaseapp.com",
    projectId: "tortbot-admin",
    storageBucket: "tortbot-admin.appspot.com",
    messagingSenderId: "705868500245",
    appId: "1:705868500245:web:d55e3d79ada103dd54ed1c"
  };
      // Initialize Firebase
      firebase.initializeApp(firebaseConfig);


document.querySelector("#logout").addEventListener("click", () => {
        signOut();
      });

const signOut = () => {
        firebase
          .auth()
          .signOut()
          .then(function () {
            location.replace('/admin');
          })
          .catch(function (error) {
            alert("error signing out, check network connection");
          });
      };