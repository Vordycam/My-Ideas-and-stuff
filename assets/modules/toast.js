export const toasts = [
  { cls: '', msg: '<strong>Match</strong> queued' },
  { cls: 'orange', msg: '<strong>Warning</strong> high ping detected' },
  { cls: 'green', msg: '<strong>Success</strong> build complete' },
];

export function showToast(i){
  const container = document.querySelector('.toast-stack');
  if(!container) return;
  const t = toasts[i % toasts.length];
  const el = document.createElement('div');
  el.className = `toast ${t.cls}`;
  el.setAttribute('role', 'status');
  el.innerHTML = `\n    <div>⬡</div>\n    <div class=\"toast-msg\">${t.msg}</div>\n  `;
  container.appendChild(el);
  setTimeout(()=>{ el.style.opacity = '0'; el.style.transition = 'opacity 0.5s'; setTimeout(()=> el.remove(), 500); }, 4000);
}
