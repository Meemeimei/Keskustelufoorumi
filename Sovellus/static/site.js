$('document').ready(function() {
  var URLparam = window.location.search.substring(1);
  if (URLparam !== "") {
    var paramType = URLparam.split('=')[0];
    if (paramType === "error")
    {
      $("#error").html(URLparam.split('=')[1].replace(/\+/g, ' '));
    } else if (paramType === "message") {
      $("#message").html(URLparam.split('=')[1].replace(/\+/g, ' '));
    }
  }
});

function displayPassword() {
  var x = document.getElementById("password");
  var y = document.getElementById("passwordRepeat");
  var z = document.getElementById("oldPassword");
  if (x.type === "password") {
    x.type = "text";
    if (y !== null) {
      y.type = "text";
    }
    if (z !== null) {
      z.type = "text";
    }
  } else {
    x.type = "password";
    if (y !== null) {
      y.type = "password";
    }
    if (z !== null) {
      z.type = "password";
    }
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

function validateAreaName() {
  if ($("#name").val() !== "") {
    $("#submitAreaButton")[0].disabled = false;
  } else {
    $("#submitAreaButton")[0].disabled = true;
  }
}

function validateGroupName() {
  if ($("#name").val() !== "") {
    $("#submitGroupButton")[0].disabled = false;
  } else {
    $("#submitGroupButton")[0].disabled = true;
  }
}

function displayEdit(selection) {
  $("#hide"+selection)[0].hidden = true;
  $("#show"+selection)[0].hidden = false;
  $("#edit"+selection).val($("#content"+selection));
}