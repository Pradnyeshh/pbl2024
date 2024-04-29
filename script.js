document.getElementById('generate-btn').addEventListener('click', function () {
    var topic = document.getElementById('topic').value;
    var reportType = document.getElementById('report-type').value;
    console.log(topic, reportType, "Data")
    fetch('http://127.0.0.1:5000/generate-content', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: {
            topic: topic,
            report_type: reportType
        }
    })
        .then(response => response.data)
        .then(data => {
            // Update frontend with received data
            console.log(data); // For debugging
            document.getElementById('output').innerText = JSON.stringify(data, null, 2);
        })
        .catch(error => {
            console.error('Error:', error);
        });
});