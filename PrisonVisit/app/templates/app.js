


var pub = localStorage.getItem('public_id');
var tokens = localStorage.getItem('token');
function visitation() {
    $.ajax(
        {

            url: "http://127.0.0.1:5000/visitation/",
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify({
                'nameP':$("#nameP").val(),
                'vDate':$("#vDate").val(),
                'numV':$("#numV").val(),
                'public_id':pub
            }),
            method: "POST",
            dataType: "json",
            crossDomain: true,
            headers: {
                        'x-access-token': tokens
                    },

            success: function (resp) {
               // alert(resp.status);
                console.log("success");
                alert("Success!");

                window.location.replace('visitation.html');
            },

            error: function (resp) {
                //window.location.replace('404.html');
                alert("kapit lang!");

            }


        }
    );

}

