async function getAllFoods(date) {
    // Send the request to the server
    const response = await fetch('/food', {
        method: 'POST',
        body: JSON.stringify({date: date}),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    return await response.json()
}

async function getAllWaters(date) {
    // Send the request to the server
    const response = await fetch('/water', {
        method: 'POST',
        body: JSON.stringify({date: date}),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    return await response.json()
}

function updateElement(elementId, data) {
    var element = document.getElementById(elementId);
    element.innerHTML = '';
    for (var item of data) {
        element.innerHTML += '<li>' + item + '</li>';
    }
}

export function getAllData() {
    var date = document.getElementById('datepicker').value;

    const foodData = getAllFoods(date)
    updateElement('foodList', foodData)

    const waterData = getAllWaters(date)
    updateElement('waterList', waterData)
}