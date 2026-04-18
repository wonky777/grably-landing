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
    var _t = typeof t === 'function' ? t : function(k){ return k; };
    var initial = user.email[0].toUpperCase();
    var balText = user.unlimited ? '\u267E\uFE0F Unlimited' : (user.coins || 0) + ' GC';
    container.innerHTML =
      '<div class="profile-menu">' +
        '<button class="profile-avatar" id="profile-btn">' + initial + '</button>' +
        '<div class="profile-dd" id="profile-dd">' +
          '<div class="profile-hd">' +
            '<div class="profile-em">' + user.email + '</div>' +
            '<div class="profile-bal">' + balText + '</div>' +
          '</div>' +
          '<a href="/profile.html" class="profile-it">\uD83D\uDC64 ' + _t('nav_profile') + '</a>' +
          '<a href="/buy.html" class="profile-it">\uD83D\uDCB0 ' + _t('nav_topup') + '</a>' +
          '<a href="#" class="profile-it" id="logout-link">\uD83D\uDEAA ' + _t('nav_logout') + '</a>' +
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
    var _t = typeof t === 'function' ? t : function(k){ return k; };
    container.innerHTML =
      '<a href="/login.html" class="btn-ghost">' + _t('nav_login') + '</a>' +
      '<a href="/GrabLy.zip" download class="btn-sm">' + _t('nav_install_btn') + '</a>';
  }
}

document.addEventListener('DOMContentLoaded', renderAuthNav);
