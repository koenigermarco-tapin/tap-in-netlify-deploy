(function(){
  // Simple i18n loader: if a ?lang=de param is present and a mapped page exists, redirect.
  // Otherwise, if translations exist for keys, apply them to elements with data-i18n.

  function getQueryParam(name) {
    const params = new URLSearchParams(window.location.search);
    return params.get(name);
  }

  function fetchJSON(path){
    return fetch(path).then(r=>{
      if(!r.ok) throw new Error('Failed to load '+path);
      return r.json();
    });
  }

  const requestedLang = getQueryParam('lang');
  if(!requestedLang) return; // no lang requested, nothing to do

  // Try to load mapping and translations in parallel
  Promise.all([
    fetchJSON('/i18n/lang-map.json').catch(()=>({})),
    fetchJSON('/i18n/translations.json').catch(()=>({}))
  ]).then(([map, translations])=>{
    const page = location.pathname.split('/').pop() || 'index.html';
    // If map has a mapping for this page and requestedLang is 'de', redirect to mapped file
    if(requestedLang !== 'en' && map && map[page]){
      const target = '/' + map[page];
      if(location.pathname.endsWith(map[page])) {
        // Already on target page (maybe user toggled), so apply translations in-place
        applyTranslations(translations, requestedLang);
      } else {
        // redirect to the mapped file, preserve hash
        const hash = location.hash || '';
        window.location.href = target + hash;
      }
      return;
    }

    // Otherwise, try to apply translations to elements with data-i18n
    applyTranslations(translations, requestedLang);
  }).catch(err=>{
    console.warn('i18n loader error', err);
  });

  function applyTranslations(translations, lang){
    if(!translations || !translations[lang]) return;
    const dict = translations[lang];
    document.querySelectorAll('[data-i18n]').forEach(el=>{
      const key = el.getAttribute('data-i18n');
      if(!key) return;
      const val = dict[key];
      if(val !== undefined){
        if(el.placeholder !== undefined && el.tagName.toLowerCase()==='input') el.placeholder = val;
        else el.textContent = val;
      }
    });
  }
})();
