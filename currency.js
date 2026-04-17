// Currency system: RUB for Russian, USD for everything else
// Exchange rate: 1 USD ≈ 100 RUB (simplified)

var GRABLY_CURRENCIES = {
  RUB: { symbol: '\u20BD', code: 'RUB', rate: 1 },
  USD: { symbol: '$', code: 'USD', rate: 0.01 }
};

// Prices in RUB (base)
var GRABLY_PRICES_RUB = {
  gc10: 100,
  gc50: 475,
  gc150: 1350,
  gc500: 4500,
  unlimited: 4990,
  per_gc: 10 // 10 RUB per 1 GC base
};

function getCurrency() {
  var stored = localStorage.getItem('grably_currency');
  if (stored && GRABLY_CURRENCIES[stored]) return stored;
  // Auto-detect from language
  var lang = localStorage.getItem('grably_lang') || (navigator.language || 'en').split('-')[0];
  return (lang === 'ru' || lang === 'uk') ? 'RUB' : 'USD';
}

function setCurrency(code) {
  if (GRABLY_CURRENCIES[code]) {
    localStorage.setItem('grably_currency', code);
  }
}

function formatPrice(rubPrice) {
  var cur = getCurrency();
  var c = GRABLY_CURRENCIES[cur];
  var val = Math.round(rubPrice * c.rate);
  if (cur === 'USD') {
    return c.symbol + val;
  }
  return val.toLocaleString() + '\u2009' + c.symbol;
}

function getCurrencySymbol() {
  return GRABLY_CURRENCIES[getCurrency()].symbol;
}

// Apply prices to elements with data-price attribute
function applyPrices() {
  document.querySelectorAll('[data-price]').forEach(function(el) {
    var key = el.getAttribute('data-price');
    var rub = GRABLY_PRICES_RUB[key];
    if (rub !== undefined) {
      el.textContent = formatPrice(rub);
    }
  });
}

document.addEventListener('DOMContentLoaded', applyPrices);
