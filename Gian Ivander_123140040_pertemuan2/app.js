import { Dashboard } from './dashboard.js';
import { $, createEl, timePad } from './utils.js';

const app = new Dashboard();

const importSample = () => {
	const sampleSchedule = [
		{ course: 'Matematika Diskrit', day: 'Senin', time: '09:00 - 11:00', room: 'R401' },
		{ course: 'Algoritma & Struktur Data', day: 'Rabu', time: '13:00 - 15:00', room: 'R202' },
		{ course: 'Sistem Operasi', day: 'Jumat', time: '10:00 - 12:00', room: 'R103' }
	];
	sampleSchedule.forEach(s => app.data.schedule.push(s));
	app.save();
	renderSchedule();
};

const onClearAll = () => {
	if (!confirm('Hapus semua data di dashboard?')) return;
	app.clearAll();
	renderAll();
};

// render helpers
function renderTasks() {
	const container = $('#tasks');
	container.innerHTML = '';
	if (!app.data.tasks.length) {
		container.innerHTML = '<div class="empty">Tidak ada tugas</div>';
		return;
	}
	app.data.tasks.forEach(t => {
		const el = createEl('div', { className: 'item' });
		const left = createEl('div', { innerHTML: `<strong>${t.title}</strong><div class="meta">${new Date(t.createdAt).toLocaleString()}</div>` });
		const actions = createEl('div', { className: 'actions' });
		const del = createEl('button', { innerText: '🗑️' });
		del.addEventListener('click', () => { app.deleteItem('tasks', t.id); renderAll(); });
		actions.appendChild(del);
		el.appendChild(left);
		el.appendChild(actions);
		container.appendChild(el);
	});
}

function renderNotes() {
	const container = $('#notes');
	container.innerHTML = '';
	if (!app.data.notes.length) { container.innerHTML = '<div class="empty">Tidak ada catatan</div>'; return; }
	app.data.notes.forEach(n => {
		const el = createEl('div', { className: 'item' });
		const left = createEl('div', { innerHTML: `<strong>${n.title}</strong><div class="meta">${new Date(n.createdAt).toLocaleString()}</div>` });
		const actions = createEl('div', { className: 'actions' });
		const del = createEl('button', { innerText: '🗑️' });
		del.addEventListener('click', () => { app.deleteItem('notes', n.id); renderAll(); });
		actions.appendChild(del);
		el.appendChild(left);
		el.appendChild(actions);
		container.appendChild(el);
	});
}

function renderSchedule() {
	const container = $('#schedule');
	container.innerHTML = '';
	if (!app.data.schedule.length) { container.innerHTML = '<div class="empty">Kosong</div>'; return; }
	app.data.schedule.forEach(s => {
		const row = createEl('div', { className: 'item' });
		row.innerHTML = `<div><strong>${s.course}</strong><div class="meta">${s.day} • ${s.time} • ${s.room}</div></div>`;
		container.appendChild(row);
	});
}

function renderAll() {
	renderTasks();
	renderNotes();
	renderSchedule();
}

// UI actions
function onAddTask() {
	const title = prompt('Judul tugas:');
	if (!title) return;
	app.addItem('tasks', { title });
	renderAll();
}

function onAddNote() {
	const title = prompt('Judul catatan:');
	if (!title) return;
	app.addItem('notes', { title });
	renderAll();
}

function onQuickAdd() {
	const input = $('#quickTitle');
	const type = $('#quickType').value;
	const title = input.value && input.value.trim();
	if (!title) return alert('Masukkan judul singkat');
	app.addItem(type === 'note' ? 'notes' : 'tasks', { title });
	input.value = '';
	renderAll();
}

// Clock
const updateClock = () => {
	const now = new Date();
	$('#time').textContent = `${timePad(now.getHours())}:${timePad(now.getMinutes())}`;
	$('#date').textContent = now.toLocaleDateString();
};

// Init
const init = async () => {
	await app.load();
	$('#addTaskBtn').addEventListener('click', onAddTask);
	$('#addNoteBtn').addEventListener('click', onAddNote);
	$('#quickAddBtn').addEventListener('click', onQuickAdd);
	$('#importSample').addEventListener('click', importSample);
	$('#clearAllBtn').addEventListener('click', onClearAll);
	document.addEventListener('keydown', (e) => { if (e.ctrlKey && e.key.toLowerCase() === 'k') { e.preventDefault(); $('#quickTitle').focus(); } });
	renderAll();
	updateClock();
	setInterval(updateClock, 1000);
};

init();

// expose for debugging
window.__dashboard = app;