function navigate(tab) {
    var tabs = document.getElementsByClassName('tab-content');
    for (var i = 0; i < tabs.length; i++) {
        tabs[i].classList.remove('active');
    }
    document.getElementById(tab).classList.add('active');
}

// Set default tab
document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('master').classList.add('active');
});
