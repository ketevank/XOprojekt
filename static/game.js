interval = setInterval(myAjax, 1000);

$(document).ready(function () {
    addAllCellEvents();
});

$('#gameslist').click(function () {
    $.ajax({
        url: '/cmd',
        type: 'GET',
        data: JSON.stringify({'cmd': cmd, 'data': data, 'playerid': playerId, 'sessionid': sessionID}),
        success: function (result) {
            renderGame(result)
        },
        error: function (err, s, exception) {
            console.log(exception);
        }
    });
})

$('#menu').click(function () {
    $.ajax({
        url: '/restart?sessionid=' + sessionID,
        type: 'GET',
        error: function (err, s, exception) {
            console.log(exception);
        }
    })
});

function addAllCellEvents() {
    for (let x = 1; x < 4; x++) {
        for (let y = 1; y < 4; y++) {
            addCellEvent(x, y);
        }
    }
}

function addCellEvent(x, y) {
    $('#js-' + x + '_' + y).click(function () {
        myAjax('mark', {x: x, y: y});
    });
}

function myAjax(cmd, data) {
    $.ajax({
        url: '/cmd',
        type: 'POST',
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({'cmd': cmd, 'data': data, 'playerid': playerId, 'sessionid': sessionID}),
        success: function (result) {
            renderGame(result)
        },
        error: function (err, s, exception) {
            console.log(exception);
        }
    });
}

function handleWin(result) {
    let players = result.players;
    for (let key in players) {
        let player = players[key];
        if (player.hasWinningPosition) {
            $("#alertWin").text("Wygrana: gracz " + player.sign);
        }
        if (player.scoreDraw) {
            $("#alertWin").text("Remis");
        }
    }
}

function renderGame(result) {
    let players = $.map(result.players, function (value, key) {
        return value
    });
    let currentPlayer = players.filter(function (player) {
        return player != result.players[result.last_move_player_id]
    });
    $("#whichPlayer").text("Gracz " + result.players[playerId].sign);
    if (players.length < 2) {
        $("#alertWin").text("Oczekiwanie na drugiego gracza");
    } else {
        $("#alertWin").text("Następny ruch: gracz " + currentPlayer[0].sign);
    }

    renderAllMarks(result);
    handleWin(result);
}

function renderAllMarks(result) {
    clearFields();
    let players = result.players;
    for (let key in players) {
        let player = players[key];
        renderPlayerMarks(player)
    }
}

function clearFields() {
    $(".cell").html("")
}

function renderPlayerMarks(player) {
    let markedFields = player.marked_fields;
    for (let key in markedFields) {
        let field = player.marked_fields[key];
        $(getCellId(field)).html(player.sign);
    }
}

function getCellId(cellData) {
    return '#js-' + cellData.x + '_' + cellData.y;
}

$.urlParam = function (name) {
    var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
    return results[1] || 0;
}

playerId = $.urlParam('playerid')
sessionID = $.urlParam('sessionid')