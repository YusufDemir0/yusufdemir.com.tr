(function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('ana-menu');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(open));
      toggle.querySelector('.label').textContent = open ? 'Kapat' : 'Menü';
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) {
        toggle.click();
        toggle.focus();
      }
    });
  }

  var stage = document.getElementById('trans-stage');
  var paper = document.getElementById('trans-paper');
  var line = document.getElementById('slider-line');
  if (!stage || !paper || !line) return;

  var percent = 50;

  function setSplit(p) {
    percent = Math.max(4, Math.min(96, p));
    paper.style.width = percent + '%';
    line.style.left = percent + '%';
    line.setAttribute('aria-valuenow', String(Math.round(percent)));
  }

  function fromX(clientX) {
    var rect = stage.getBoundingClientRect();
    setSplit(((clientX - rect.left) / rect.width) * 100);
  }

  function syncWidth() {
    stage.style.setProperty('--stage-w', stage.clientWidth + 'px');
  }
  syncWidth();
  window.addEventListener('resize', syncWidth);

  stage.addEventListener('mousemove', function (e) { fromX(e.clientX); });
  stage.addEventListener('touchstart', function (e) {
    if (e.touches[0]) fromX(e.touches[0].clientX);
  }, { passive: true });
  stage.addEventListener('touchmove', function (e) {
    if (e.touches[0]) fromX(e.touches[0].clientX);
  }, { passive: true });

  line.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowLeft') { setSplit(percent - 5); e.preventDefault(); }
    if (e.key === 'ArrowRight') { setSplit(percent + 5); e.preventDefault(); }
  });
})();
