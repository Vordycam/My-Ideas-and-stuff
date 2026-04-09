import { startFeed } from './modules/feed.js';
import { showToast } from './modules/toast.js';
import { initUI } from './modules/ui.js';

window.addEventListener('DOMContentLoaded', ()=>{
  try{ initUI(); }catch(e){/* noop */}
  try{ startFeed(); }catch(e){/* noop */}
  setTimeout(()=>{ try{ showToast(0); }catch(e){} }, 1500);
  setTimeout(()=>{ try{ showToast(1); }catch(e){} }, 5000);
  setTimeout(()=>{ try{ showToast(2); }catch(e){} }, 9000);
});
