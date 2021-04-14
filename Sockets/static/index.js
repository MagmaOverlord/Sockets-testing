$(document).ready(function () {
    var socket = io.connect("http://" + document.domain+":"+location.port+"/test");

    socket.on("my connection", function (msg) {
        $("#log").append("<p style = 'color: green'>Status: " + msg.data + "</p>");
    });
    socket.on("new message", function (msg) {
        $("#log").append("<p>Recieved: " + msg.data + "</p>");
    });

    $("#message").submit(function (event) {
        socket.emit("my new message", { data: $("#message_data").val() });
        document.getElementById("message").reset();

        return false;
    });

});