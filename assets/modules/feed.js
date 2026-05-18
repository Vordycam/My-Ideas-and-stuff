export function startFeed(containerId = 'liveFeed'){
  const feedItems = [
    { t: '2:10', msg: "<strong>Radiant</strong> claimed the top shrine" },
    { t: '2:45', msg: "<strong>StreamTeam</strong> got first blood on <span class=\"hl\">Mid Tower</span>" },
    { t: '3:12', msg: "<strong>ProSquad</strong> completed a perfect rotation" },
    { t: '3:58', msg: "<strong>PubPlayer</strong> pulled a clutch <span class=\"hl-gold\">Double Kill</span>" },
  ];

  const container = document.getElementById(containerId);
  if(!container) return;
  let idx = 0;
  setInterval(()=>{
    const it = feedItems[idx++ % feedItems.length];
    const node = document.createElement('div');
    node.className = 'feed-item';
    node.innerHTML = `<div class=\"feed-time\">${it.t}</div><div class=\"feed-text\">${it.msg}</div>`;
    container.prepend(node);
    while(container.children.length > 8) container.removeChild(container.lastChild);
  }, 4000);
}
