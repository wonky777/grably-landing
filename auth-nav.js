var GRABLY_API = 'https://grably-server-production.up.railway.app';

function getOrCreateDeviceId() {
  var id = localStorage.getItem('grably_device_id');
  if (!id) {
    id = 'web_' + Array.from(crypto.getRandomValues(new Uint8Array(16)))
      .map(function(b){return b.toString(16).padStart(2,'0')}).join('');
    localStorage.setItem('grably_device_id', id);
  }
  return id;
}

function renderAuthNav() {
  var user = JSON.parse(localStorage.getItem('grably_user') || 'null');
  var container = document.getElementById('auth-nav');
  if (!container) return;

  if (user) {
    var initial = user.email[0].toUpperCase();
    container.innerHTML =
      '<div class="profile-menu">' +
        '<button class="profile-avatar" id="profile-btn">' + initial + '</button>' +
        '<div class="profile-dd" id="profile-dd">' +
          '<div class="profile-hd">' +
            '<div class="profile-em">' + user.email + '</div>' +
            '<div class="profile-bal">' + (user.unlimited ? '\u267E\uFE0F \u0411\u0435\u0437\u043B\u0438\u043C\u0438\u0442' : (user.coins || 0) + ' GC') + '</div>' +
          '</div>' +
          '<a href="/profile.html" class="profile-it">\uD83D\uDC64 \u041F\u0440\u043E\u0444\u0438\u043B\u044C</a>' +
          '<a href="/#pricing" class="profile-it">\uD83D\uDCB0 \u041F\u043E\u043F\u043E\u043B\u043D\u0438\u0442\u044C</a>' +
          '<a href="#" class="profile-it" id="logout-link">\uD83D\uDEAA \u0412\u044B\u0439\u0442\u0438</a>' +
        '</div>' +
      '</div>';

    document.getElementById('profile-btn').addEventListener('click', function(e) {
      e.stopPropagation();
      document.getElementById('profile-dd').classList.toggle('open');
    });
    document.getElementById('logout-link').addEventListener('click', function(e) {
      e.preventDefault();
      localStorage.removeItem('grably_user');
      window.location.href = '/';
    });
    document.addEventListener('click', function() {
      var dd = document.getElementById('profile-dd');
      if (dd) dd.classList.remove('open');
    });
  } else {
    container.innerHTML =
      '<a href="/login.html" class="btn-ghost">\u0412\u043E\u0439\u0442\u0438</a>' +
      '<a href="/GrabLy.zip" download class="btn-sm">\u0421\u043A\u0430\u0447\u0430\u0442\u044C</a>';
  }
}

document.addEventListener('DOMContentLoaded', renderAuthNav);
