
var firebaseConfig = {
    apiKey: "AIzaSyD9PHYtbLP3qrHMKsW7H-13oyyBxbV5eJA",
    authDomain: "enigma-or.firebaseapp.com",
    databaseURL: "https://enigma-or.firebaseio.com",
    projectId: "enigma-or",
    storageBucket: "",
    messagingSenderId: "750308248587",
    appId: "1:750308248587:web:79b32f294451de0ad38b0e"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);


  
//   Auth

  var name;
  var email ;
  var ans ;


function onSignIn(googleUser) {
    
    var profile = googleUser.getBasicProfile();
    console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
    console.log('Name: ' + profile.getName());
    console.log('Image URL: ' + profile.getImageUrl());
    console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
    email = String(profile.getEmail());
    name = profile.getName();
    console.log(name);
    console.log(email);
    document.getElementById("signin").style.display="none" ;
    document.getElementById("aftersignin").style.display="block";
    document.getElementById("welcome").style.display="block";
    document.getElementById("welcome").innerHTML += " "+name;

    // var id_token = googleUser.getAuthResponse().id_token ;
    // console.log("ID Token: " + id_token);

    var password = "asdf1234";

    

    firebase.auth().signInWithEmailAndPassword(email, password).catch(function(error) {
      console.log("Account already exist");

      var errorCode = error.code;
      var errorMessage = error.message;
      if(errorCode != null){

        firebase.auth().createUserWithEmailAndPassword(email, password).catch(function(error) {
          // Handle Errors here.
          var errorCode = error.code;
          var errorMessage = error.message;
          // ...
        });
      
      }
    });

    firebase.auth().onAuthStateChanged(function(user) {
      if (user) {
        console.log(user.uid);
        var database = firebase.database();
        console.log(database);
        var ref = database.ref();
        ref.child(user.uid+"/name").set(name);
        ref.child(user.uid+"/email").set(email);

      } else {
        // No user is signed in.
      }
    });



}

function signOut() {
    console.log(email);
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
      console.log('User signed out.');
    });
  }
  
  function riddle(){
    window.location.href = "./Riddle.html";
  }

  
function data(){

  document.getElementById("loding").style.display = "block";
  document.getElementById("ans").style.display = "none";
  document.getElementById("riddletext").style.display = "none";
    
    ans = document.getElementById("sol").value;
    console.log(ans);
    if(ans != ""){
      firebase.auth().onAuthStateChanged(function(user) {
        if (user) {
          console.log(user.uid);
          var database = firebase.database();
          console.log(database);
          var ref = database.ref();
          ref.child(user.uid+"/ans").set(ans);
        
  
        } else {
          // No user is signed in.
        }
      });
  







      changeLocation ();
      
        
        //                 ref.child("User "+snapshot.val()+"/name").set(name);
        //                 ref.child("User "+snapshot.val()+"/ans").set(ans);
        //                 ref.child("User "+snapshot.val()+"/email").set(email);
        // ref.child("sl").set(1+snapshot.val());

    }

    
    
}


// function towelcome(){
  // var database = firebase.database();
  // console.log(database);
  // var ref = database.ref();
  
//   var 


// }







function changeLocation (){
  setTimeout(function(){
   window.location = "./thankyou.html";
  },5000);
 }



