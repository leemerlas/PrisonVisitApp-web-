function comments() {
    $.ajax(
        {
            url: "http://127.0.0.1:5000/comments/",
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify({
                'cid': $("#cid").val(),
                'vid': $("#vid").val(),
                'content': $("#content").val(),
                'date': $("#date").val()
            }),
            method: "POST",
            dataType: "json",
            crossDomain: true,

            success: function (resp) {
               // alert(resp.status);
                console.log("success");

                window.location.replace('success.html');
            },

            error: function (resp) {
                //window.location.replace('404.html');
                alert("Oops! Something went wrong.");

            }


        }
    );

}