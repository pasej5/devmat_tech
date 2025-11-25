// Toast Notification Script
const successToast = document.getElementById('success-toast');
if (successToast) {
  setTimeout(() => {
    successToast.classList.add('show');
  }, 100);
  setTimeout(() => {
    successToast.classList.remove('show');
  }, 5000);
}

// Tab Functionality Script
var tablinks = document.getElementsByClassName('tab-links');
var tabcontents = document.getElementsByClassName('tab-contents');

function opentab(tabname) {
  for (tablink of tablinks) {
    tablink.classList.remove('active-link');
  }
  for (tabcontent of tabcontents) {
    tabcontent.classList.remove('active-tab');
  }
  event.currentTarget.classList.add('active-link');
  document.getElementById(tabname).classList.add('active-tab');
}

// Sidebar Menu Script
var sidemenu = document.getElementById('sidemenu');
function openmenu() {
  sidemenu.style.right = '0';
}
function close() {
  sidemenu.style.right = '-200px';
}
