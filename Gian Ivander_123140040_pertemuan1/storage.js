const STORAGE_KEY = 'college_tasks_v2';


export function loadTasks() {
try {
const raw = localStorage.getItem(STORAGE_KEY);
const arr = raw ? JSON.parse(raw) : [];
return Array.isArray(arr) ? arr : [];
} catch (e) {
console.error('Gagal memuat tasks', e);
return [];
}
}


export function saveTasks(tasks) {
try {
localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks));
} catch (e) {
console.error('Gagal menyimpan tasks', e);
}
}