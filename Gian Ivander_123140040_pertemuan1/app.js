import { loadTasks, saveTasks } from './storage.js';
import { formatDateISO, isValidDate } from './utils.js';

let tasks = [];
let editingId = null;

function $(id) { return document.getElementById(id); }

function escapeHtml(s) {
  return String(s || '')
    .replaceAll('&','&amp;')
    .replaceAll('<','&lt;')
    .replaceAll('>','&gt;')
    .replaceAll('"','&quot;')
    .replaceAll("'",'&#039;');
}

function buildCourseOptions() {
  const sel = $('filterCourse');
  if (!sel) return;
  const prev = sel.value;
  const courses = Array.from(new Set(tasks.map(t => (t.course || '').trim()).filter(Boolean))).sort((a,b)=>a.localeCompare(b));
  sel.innerHTML = '<option value="all">Semua Mata Kuliah</option>' + courses.map(c => `<option value="${escapeHtml(c)}">${escapeHtml(c)}</option>`).join('');
  if ([...sel.options].some(o => o.value === prev)) sel.value = prev;
}


function render() {
  const tbody = document.querySelector('#taskTable tbody');
  if (!tbody) { console.warn('render: tbody not found'); return; }

  const status = $('filterStatus') ? $('filterStatus').value : 'all';
  const courseFilter = $('filterCourse') ? $('filterCourse').value : 'all';
  const q = $('searchTask') ? $('searchTask').value.trim().toLowerCase() : '';

  const left = tasks.filter(t => !t.done).length;
  if ($('leftCount')) $('leftCount').textContent = String(left);

  let shown = tasks.slice();
  if (status === 'done') shown = shown.filter(t => t.done);
  if (status === 'notdone') shown = shown.filter(t => !t.done);
  if (courseFilter !== 'all') shown = shown.filter(t => t.course === courseFilter);
  if (q) shown = shown.filter(t => (t.name||'').toLowerCase().includes(q) || (t.course||'').toLowerCase().includes(q));

  shown.sort((a,b)=>{
    const ad = a.deadline ? new Date(a.deadline).getTime() : Infinity;
    const bd = b.deadline ? new Date(b.deadline).getTime() : Infinity;
    return ad - bd;
  });

  if (!shown.length) {
    tbody.innerHTML = '<tr><td colspan="6" class="small">Tidak ada tugas.</td></tr>';
    buildCourseOptions();
    return;
  }

  tbody.innerHTML = shown.map(t => `
    <tr class="${t.done ? 'done' : 'notdone'}" data-id="${t.id}">
      <td><input type="checkbox" class="toggle-done" data-id="${t.id}" ${t.done ? 'checked' : ''}></td>
      <td><strong>${escapeHtml(t.name)}</strong></td>
      <td>${escapeHtml(t.course)}</td>
      <td>${formatDateISO(t.deadline)}</td>
      <td>${escapeHtml(t.note || '')}</td>
      <td>
        <button class="edit-btn" data-edit="${t.id}" aria-label="Edit">✏️</button>
        <button class="del-btn" data-del="${t.id}" aria-label="Hapus">🗑️</button>
      </td>
    </tr>`).join('');

  buildCourseOptions();
}

function openModal(editId = null) {
  const dialog = $('taskModal');
  const form = $('taskForm');
  if (!dialog || !form) return;

  if ($('errName')) $('errName').hidden = true;
  if ($('errCourse')) $('errCourse').hidden = true;
  if ($('errDeadline')) $('errDeadline').hidden = true;

  if (editId) {
    const t = tasks.find(x => x.id === editId);
    if (!t) return;
    $('modalTitle').textContent = 'Edit Tugas';
    $('taskName').value = t.name || '';
    $('taskCourse').value = t.course || '';
    $('taskDeadline').value = t.deadline || '';
    $('taskNote').value = t.note || '';
    editingId = editId;
  } else {
    form.reset();
    $('modalTitle').textContent = 'Tambah Tugas';
    editingId = null;
  }

  try { dialog.showModal(); } catch (err) { dialog.setAttribute('open',''); $('taskName').focus(); }
}

function closeModal() {
  const dialog = $('taskModal');
  if (!dialog) return;
  try { dialog.close(); } catch (e) { dialog.removeAttribute('open'); }
  editingId = null;
}

function validateForm(name, course, deadline) {
  let ok = true;
  if (!name) { if ($('errName')) $('errName').hidden = false; ok = false; } else if ($('errName')) $('errName').hidden = true;
  if (!course) { if ($('errCourse')) $('errCourse').hidden = false; ok = false; } else if ($('errCourse')) $('errCourse').hidden = true;
  if (!deadline || !isValidDate(deadline)) { if ($('errDeadline')) $('errDeadline').hidden = false; ok = false; } else if ($('errDeadline')) $('errDeadline').hidden = true;
  return ok;
}

function attachEvents() {
  const addBtn = $('addTaskBtn');
  if (addBtn) addBtn.addEventListener('click', (e) => { e.preventDefault(); openModal(); });

  const cancelBtn = $('cancelBtn');
  if (cancelBtn) cancelBtn.addEventListener('click', (e) => { e.preventDefault(); closeModal(); });

  const form = $('taskForm');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const nameEl = $('taskName'); const courseEl = $('taskCourse'); const deadlineEl = $('taskDeadline'); const noteEl = $('taskNote');
      const name = nameEl ? nameEl.value.trim() : '';
      const course = courseEl ? courseEl.value.trim() : '';
      const deadline = deadlineEl ? deadlineEl.value : '';
      const note = noteEl ? noteEl.value.trim() : '';

      if (!validateForm(name, course, deadline)) return;

      if (editingId) {
        const idx = tasks.findIndex(t => t.id === editingId);
        if (idx !== -1) {
          tasks[idx] = { ...tasks[idx], name, course, deadline, note };
        } else {
          console.warn('submit: editingId not found, creating new instead');
          tasks.push({ id: Date.now().toString(), name, course, deadline, note, done: false, createdAt: new Date().toISOString() });
        }
      } else {
        tasks.push({ id: Date.now().toString(), name, course, deadline, note, done: false, createdAt: new Date().toISOString() });
      }

      saveTasks(tasks);
      render();
      closeModal();
    });
  } else {
    console.warn('attachEvents: taskForm not found');
  }

  const filterStatus = $('filterStatus');
  if (filterStatus) filterStatus.addEventListener('change', render);

  const filterCourse = $('filterCourse');
  if (filterCourse) filterCourse.addEventListener('change', render);

  const search = $('searchTask');
  if (search) search.addEventListener('input', () => setTimeout(render, 150));

  const tbody = document.querySelector('#taskTable tbody');
  if (tbody) {
    tbody.addEventListener('click', (e) => {
      const delBtn = e.target.closest('[data-del]');
      const editBtn = e.target.closest('[data-edit]');
      const toggle = e.target.closest('.toggle-done');

      if (toggle) {
        const id = toggle.dataset.id;
        const t = tasks.find(x => x.id === id);
        if (t) {
          t.done = !!toggle.checked;
          saveTasks(tasks);
          render();
        }
        return;
      }

      if (delBtn) {
        const id = delBtn.dataset.del;
        const t = tasks.find(x => x.id === id);
        if (!t) return;
        if (!confirm(`Hapus tugas \"${t.name}\"?`)) return;
        tasks = tasks.filter(x => x.id !== id);
        saveTasks(tasks);
        render();
        return;
      }

      if (editBtn) {
        const id = editBtn.dataset.edit;
        openModal(id);
        return;
      }
    });
  } else {
    console.warn('#taskTable tbody not found when attaching click handler');
  }
}

function init() {
  try {
    tasks = loadTasks() || [];
  } catch (e) {
    console.error('init: loadTasks failed', e);
    tasks = [];
  }
  attachEvents();
  render();
}

window.addEventListener('DOMContentLoaded', init);
