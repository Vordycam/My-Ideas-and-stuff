/* Minimal JS behavior extracted from index.html */

function toggleChip(el){
  if(!el) return;
  el.classList.toggle('active');
}

// Live feed simulation
const feedItems = [
  {t: '2:10', msg: "<strong>Radiant</strong> claimed the top shrine"},
  {t: '2:45', msg: "<strong>StreamTeam</strong> got first blood on <span class=\"hl\">Mid Tower</span>"},
  {t: '3:12', msg: "<strong>ProSquad</strong> completed a perfect rotation"},
  {t: '3:58', msg: "<strong>PubPlayer</strong> pulled a clutch <span class=\"hl-gold\">Double Kill</span>"},
];

(function startFeed(){
  const container = document.getElementById('liveFeed');
  if(!container) return;
  let idx = 0;
  setInterval(()=>{
    const it = feedItems[idx++ % feedItems.length];
    const node = document.createElement('div');
    node.className = 'feed-item';
    node.innerHTML = `<div class=\"feed-time\">${it.t}</div><div class=\"feed-text\">${it.msg}</div>`;
    container.prepend(node);
    // keep max items
    while(container.children.length > 8) container.removeChild(container.lastChild);
  }, 4000);
})();

// Toast system
const toasts = [
  {lvl:'default', msg: '<strong>Match</strong> queued'},
  {lvl:'orange', msg: '<strong>Warning</strong> high ping detected'},
  {lvl:'green', msg: '<strong>Success</strong> build complete'},
];

function showToast(i){
  const container = document.querySelector('.toast-stack');
  if(!container) return;
  const t = toasts[i % toasts.length];
  const el = document.createElement('div');
  el.className = `toast ${t.lvl}`;
  el.setAttribute('role', 'status');
  el.innerHTML = `<div class=\"toast-msg\">${t.msg}</div>`;
  container.appendChild(el);
  setTimeout(()=> el.classList.add('fade'), 3800);
  setTimeout(()=> el.remove(), 4200);
}

// Small initialization
window.addEventListener('DOMContentLoaded', ()=>{
  document.querySelectorAll('.filter-chip').forEach(c=> c.addEventListener('click', ()=> toggleChip(c)));
  document.querySelectorAll('.nav .btn').forEach(b=> b.addEventListener('click', ()=> b.blur()));
});
