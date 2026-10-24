(function () {
  // Telefonda açılır menü
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('ana-menu');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Menüyü kapat' : 'Menüyü aç');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) {
        toggle.click();
        toggle.focus();
      }
    });
  }

  // Yanan kâğıt: görünür olunca bir kez oynar; "Tekrar oynat" baştan başlatır
  var stage = document.querySelector('.burn-stage');
  if (!stage) return;
  var replay = document.querySelector('.replay');
  var DURATION = 3200;
  var END = 0.8; // köşelerde yanık kâğıt parçası kalsın
  var raf = 0;

  function ease(t) { return t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2; }

  function play() {
    cancelAnimationFrame(raf);
    var start = 0;
    stage.style.setProperty('--b', '0');
    function step(now) {
      if (!start) start = now;
      var t = Math.min(1, (now - start) / DURATION);
      stage.style.setProperty('--b', (ease(t) * END).toFixed(4));
      if (t < 1) raf = requestAnimationFrame(step);
    }
    raf = requestAnimationFrame(step);
  }

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    stage.style.setProperty('--b', String(END));
  } else if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      if (entries[0].isIntersecting) {
        io.disconnect();
        setTimeout(play, 400);
      }
    }, { threshold: 0.5 });
    io.observe(stage);
  } else {
    play();
  }

  if (replay) replay.addEventListener('click', play);
})();
