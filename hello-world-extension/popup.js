document.addEventListener('DOMContentLoaded', function() {
    var fetchValueBtn = document.getElementById('fetchValueBtn');
    var valueDisplay = document.getElementById('valueDisplay');

    fetchValueBtn.addEventListener('click', function() {
        chrome.storage.local.get('myValue', function(result) {
            valueDisplay.textContent = 'Stored value: ' + result.myValue;
        });
    });
});
