$.connection.hub.start(function () {
    console.log("connected to hub");
})
$.connection.fireNotificationHub.client.fireAlert = function (fireData) {
    text = "Fire Detected !!! \n" + "Fire Rate : " + fireData.fireRate + "\n" + "Smoke Rate : " + fireData.smokeRate + " \n" + "Temperature : " + fireData.temp;
    alert(text);
    window.location.replace("http://localhost:10763/Home/Index");
}