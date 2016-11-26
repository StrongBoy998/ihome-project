function logout() {
    $.get("/api/logout", function(data){
        if (0 == data.errno) {
            location.href = "/";
        }
    })
}

$(document).ready(function(){
	$.get("/api/profile/info", function(data){
        if (0 == data.errno) {
            $("#user-name").html(data.name);
            $("#user-mobile").html(data.mobile);
            $("#user-avatar").attr("src",data.url);
        }
    })
})
