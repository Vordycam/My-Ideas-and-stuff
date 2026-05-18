export function toggleChip(el){
  if(!el) return;
  const row = el.closest('.filter-row');
  if(row){
    row.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
    el.classList.add('active');
  } else {
    el.classList.toggle('active');
  }
}

export function initUI(){
  document.querySelectorAll('.filter-chip').forEach(c => c.addEventListener('click', ()=> toggleChip(c)));
  document.querySelectorAll('.nav .btn').forEach(b => b.addEventListener('click', ()=> b.blur()));
}
