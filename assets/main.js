(() => {
  'use strict';
  const list = document.getElementById('publication-list');
  const papers = [...list.querySelectorAll('.publication')];
  const controls = document.querySelector('.publication-controls');
  const buttons = [...document.querySelectorAll('[data-mode]')];
  const search = document.getElementById('paper-search');
  const area = document.getElementById('paper-area');
  const showAll = document.getElementById('show-all');
  const count = document.getElementById('paper-count');
  let mode = 'selected';
  function filter() {
    const query = search.value.trim().toLowerCase();
    let visible = 0;
    for (const paper of papers) {
      // A search or topic selection explores the complete publication list.
      const matchesMode = query || area.value !== 'all' || mode === 'all' || paper.dataset.selected === 'true';
      const matchesArea = area.value === 'all' || paper.dataset.area === area.value;
      const matchesQuery = paper.textContent.toLowerCase().includes(query);
      paper.hidden = !(matchesMode && matchesArea && matchesQuery);
      if (!paper.hidden) visible++;
    }
    count.textContent = `${visible} ${visible === 1 ? 'paper' : 'papers'}`;
    document.getElementById('no-results').hidden = visible > 0;
    showAll.hidden = mode === 'all' || Boolean(query) || area.value !== 'all';
    buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.mode === mode)));
  }
  buttons.forEach(button => button.addEventListener('click', () => {
    mode = button.dataset.mode;
    search.value = '';
    area.value = 'all';
    filter();
  }));
  search.addEventListener('input', filter);
  area.addEventListener('change', filter);
  showAll.addEventListener('click', () => {
    mode = 'all';
    filter();
    document.getElementById('publications').scrollIntoView({behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth'});
    buttons.find(button => button.dataset.mode === 'all').focus({preventScroll: true});
  });
  controls.hidden = false;
  filter();
  const navLinks = [...document.querySelectorAll('nav a')];
  const sections = navLinks.map(link => document.querySelector(link.getAttribute('href')));
  function updateNavigation() {
    const threshold = document.querySelector('.masthead').offsetHeight + 85;
    let active = sections[0];
    sections.forEach(section => { if (section.getBoundingClientRect().top <= threshold) active = section; });
    navLinks.forEach(link => {
      const selected = link.getAttribute('href') === `#${active.id}`;
      link.classList.toggle('active', selected);
      if (selected) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
  }
  let scheduled = false;
  window.addEventListener('scroll', () => {
    if (!scheduled) requestAnimationFrame(() => { updateNavigation(); scheduled = false; });
    scheduled = true;
  }, {passive: true});
  updateNavigation();
})();
