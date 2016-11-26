function showSuccessMsg() {
    $('.save_success').fadeIn('fast', function() {
        setTimeout(function(){
            $('.save_success').fadeOut('fast',function(){}); 
        },1000) 
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){


    $.get("/api/profile/info", function(data){
        if (0 == data.errno) {
            $("#user-name").val(data.name);
            // $("#user-mobile").html(data.mobile);
            $("#user-avatar").attr("src",data.url);
        }
    })
    //上传头像

    // $("user-avatar")
    $("#form-avatar").submit(function(e){
        e.preventDefault();
        $('.image_uploading').fadeIn('fast');
        var options = {
            url:"/api/profile/avatar",
            type:"POST",
            headers:{
                "X-XSRFTOKEN":getCookie("_xsrf"),
            },
            success: function(data){
                if ("0" == data.errno) {
                    $('.image_uploading').fadeOut('fast');
                    $("#user-avatar").attr("src", data.url);
                }
            }
        };
        $(this).ajaxSubmit(options);
    });
    $("#form-name").submit(function(e){
        e.preventDefault();
        $.ajax({
          url:"/api/profile/name",
          type:"POST",
          data: JSON.stringify({username:$("#user-name").val()}),
          contentType: "application/json",
          dataType: "json",
          headers: {
              "X-XSRFTOKEN":getCookie("_xsrf"),
          },
          success: function (data) {
              if ("0" == data.errno) {
                  $("#user-name").val(data.username)
              }
              else{
                $("#user-name").val("false")
              }

          }
      });
    });
})