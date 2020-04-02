$('document').ready(function() {

});

function displayPassword() {
  var x = document.getElementById("password");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}

function checkPassword() {
  var p1 = $("#password").val();
  var p2 = $("#passwordRepeat").val();
  if (p1 === "" || p2 === "") {
    $("#submitButton")[0].disabled = true;
    return
  }

  if (p1 === p2) {
    $("#error").html("");
    if ($("#username").val() !== "") {
      $("#submitButton")[0].disabled = false;
    } else {
      $("#submitButton")[0].disabled = true;
    }
  } else {
    $("#error").html("Passwords did not match");
    $("#submitButton")[0].disabled = true;
  }
}