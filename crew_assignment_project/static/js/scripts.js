```javascript
// AJAX calls to Django views
function getCrewMembers() {
    $.ajax({
        url: '/get_crew_members/',
        type: 'GET',
        success: function(response) {
            console.log("CREW_FETCH_SUCCESS");
            // Handle the response here
        },
        error: function(error) {
            console.log(error);
        }
    });
}

function getShips() {
    $.ajax({
        url: '/get_ships/',
        type: 'GET',
        success: function(response) {
            console.log("SHIP_FETCH_SUCCESS");
            // Handle the response here
        },
        error: function(error) {
            console.log(error);
        }
    });
}

function assignCrewToShips() {
    $.ajax({
        url: '/assign_crew_to_ships/',
        type: 'POST',
        success: function(response) {
            console.log("ASSIGNMENT_SUCCESS");
            // Handle the response here
        },
        error: function(error) {
            console.log("ASSIGNMENT_FAILURE");
            console.log(error);
        }
    });
}

// Event listeners
$(document).ready(function() {
    $('#fetchCrewButton').click(getCrewMembers);
    $('#fetchShipsButton').click(getShips);
    $('#assignButton').click(assignCrewToShips);
});
```