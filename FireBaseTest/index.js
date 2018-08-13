firebase.auth().onAuthStateChanged(function(user) {
  if (user) {
    // User is signed in.
    document.GetElementById("user_div").style.display ="block";
    document.GetElementById("login_div").style.display ="none";


  } else {
    // No user is signed in.

    document.GetElementById("user_div").style.display ="none";
    document.GetElementById("login_div").style.display ="block";
  }
});

function login() {

  var userEmail = document.getElementById("email_field").value;
  var userPass = document.getElementById("password_field").value;

  firebase.auth().signInWithEmailAndPassword(userEmail, userPass).catch(function(error) {
    // Handle Errors here.
    var errorCode = error.code;
    var errorMessage = error.message;

    // ...
});
}