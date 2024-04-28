document.getElementById('generate-btn').addEventListener('click', function() {
    var topic = document.getElementById('topic').value;
    var reportType = document.getElementById('report-type').value;

    fetch('/generate-content', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 
            topic: topic,
            report_type: reportType
        })
    })
    .then(response => response.json())
    .then(data => {
        // Update frontend with received data
        console.log(data); // For debugging
        document.getElementById('output').innerText = JSON.stringify(data, null, 2);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});