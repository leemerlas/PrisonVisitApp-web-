/**
 * Created by Lee on 3/12/2018.
 */
var username = $("#username").val();
var password = $("#password").val();

function make_base_auth(user, password) {
  var tok = user + ':' + password;
  var hash = btoa(tok);
  return "Basic " + hash;
}

var auth = make_base_auth(username,password);

function login() {
    $.ajax({
        url: "http://127.0.0.1:5000/login/",
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify({
            'username': username,
            'password': password
        }),
        method: "GET",
        dataType: "json",
        crossDomain: true,
        headers: {
            'Authorization' : 'Basic ' + btoa(username + ':' + password)
        },
        // beforeSend: function (xhr) {
        //     xhr.setRequestHeader("Authorization", auth)
        // },
        success: function(resp) {
            console.log("success");
            localStorage.setItem('token', resp.token);
            window.location.replace('landing_visitor.html');
            alert.message('login success!')
        },
        error: function () {
            console.log('error')
        }
    })
}
