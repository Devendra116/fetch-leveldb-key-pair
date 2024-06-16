chrome.runtime.onInstalled.addListener(function() {
    chrome.storage.local.set({ "myValue": "Hello, Buddy!" }, function() {
        console.log('Value stored: Hello, Buddy!');
    });
});
