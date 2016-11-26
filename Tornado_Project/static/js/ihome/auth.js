function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}




function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}
$(document).ready(function(){
	$.get("/api/profile/info", function(data){
        if (0 == data.errno) {
					  $("#real-name").val(data.real_name);
					  $("#id-card").val(data.id_card);
					  $(".btn-success").hide()
        }
    })

	$("#form-auth").submit(function(e){
	      e.preventDefault();
	      realname = $("#real-name").val();
	      idcard = $("#id-card").val();
	      data = {
	      	real_name:realname,
	      	id_card:idcard,
	      }
        $.ajax({
          url:"/api/profile/realname",
          type:"POST",
          data: JSON.stringify(data),
          contentType: "application/json",
          dataType: "json",
          headers: {
              "X-XSRFTOKEN":getCookie("_xsrf"),
          },
          success: function (data) {
              if ("0" == data.errno) {
                  $("#real-name").val(data.real_name);
					  			$("#id-card").val(data.id_card);
					  			$(".btn-success").hide()
              }


          }
	      });
	    });
	  });