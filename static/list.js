interval = setInterval(fetchGames, 1000);


function fetchGames() {
    $.ajax({
        url: '/gameslist',
        type: 'GET',
        dataType: 'json',
        success: function (result) {
            renderGames(result)
        },
        error: function (err, s, exception) {
            console.log(exception);
        }
    });
}

function createGames() {
    $.ajax({
        url: '/newsession',
        type: 'GET',
        dataType: 'json',
        error: function (err, s, exception) {
            console.log(exception);
        }
    });
}

$("#joinalert").click(function () {
        $.ajax({
            url: "/newsession",
            type: 'GET',
            error: function (err, s, exception) {
                console.log(exception);
            }
        });
});



function renderGames(gameList) {
    $("#gameslist").html("")
    for (let key in gameList) {
        let sessionId = gameList[key];
        $("#gameslist").append("<div class='gameon' id='" + sessionId + "'>" + "Dołącz do gry</div>");
    }

    $(".gameon").click(function () {
        let sessionId = $(this).attr("id");
        $.ajax({
            url: "/joingame?sessionid=" + sessionId,
            dataType: 'json',
            type: 'GET',
            success: function (result) {
                let playerId = result["playerid"];
                window.open("/?sessionid=" + sessionId + "&playerid=" + playerId, '_blank');
            },
            error: function (err, s, exception) {
                console.log(exception);
            }
        });
    })
}
