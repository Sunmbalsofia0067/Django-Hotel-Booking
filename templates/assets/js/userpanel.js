var roomsData;
getAllRoomData();

function roomSelect() {
    var roomID = $("#selectRooms").val();
    setRoomDataDiv(parseInt(roomID));
}

function getAllRoomData() {
    $.ajax({
        type: 'GET',
        url: '/get_all_rooms',
        success: function (res) {
            roomsData = res.rooms
            console.log(res)
        }
    })
}

function setRoomDataDiv(id) {
    for (let i = 0; i < roomsData.length; i++) {
        if (roomsData[i].pk == id) {
            $('#roomDescription').text(roomsData[i].fields.description);
            switch (roomsData[i].fields.status) {
                case 0:
                    $('#roomStatus').html('<h3 class="text-success text-center">AVAILABLE</h3>');
                    break;
                case 1:
                case 3:
                    $('#roomStatus').html('<h3 class="text-danger text-center">UNAVAILABLE</h3>');
                    break;
                case 2:
                    $('#roomStatus').html('<h3 class="text-warning text-center">UNDER MAINTENANCE</h3>');
                    break;
                default:
                    $('#roomStatus').html('<h3 class="text-danger text-center">INVALID</h3>');
            }
            switch (roomsData[i].fields.category) {
                case 0:
                    $('#roomType').text('STANDARD');
                    break;
                case 1:
                    $('#roomType').text('ECONOMY');
                    break;
                case 2:
                    $('#roomType').text('PREMIUM');
                    break;
                case 3:
                    $('#roomType').text('SUITE');
                    break;
                default:
                    $('#roomType').text('INVALID');
            }
            $('#roomPrice').text(roomsData[i].fields.price + '/Night');
        } else {
            $('#roomDescription').text('');
            $('#roomPrice').text('');
            $('#roomType').text('');
            $('#roomStatus').text('');
        }
    }
}