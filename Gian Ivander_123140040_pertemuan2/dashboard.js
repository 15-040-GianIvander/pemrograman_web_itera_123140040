const STORAGE_KEY = 'personal_dashboard_v1';


export class Dashboard {
constructor() {
this.data = { tasks: [], notes: [], schedule: [] };
}


// async load (simulasi delay) menggunakan async/await
async load() {
const loaded = await new Promise((resolve) => {
setTimeout(() => {
const raw = localStorage.getItem(STORAGE_KEY);
resolve(raw ? JSON.parse(raw) : null);
}, 150);
});
if (loaded) this.data = loaded;
}


save() {
localStorage.setItem(STORAGE_KEY, JSON.stringify(this.data));
}


addItem(type, payload) {
const id = Date.now() + Math.random().toString(36).slice(2,6);
this.data[type].push(Object.assign({ id, createdAt: new Date().toISOString() }, payload));
this.save();
return id;
}


updateItem(type, id, patch) {
const idx = this.data[type].findIndex(i => i.id === id);
if (idx === -1) return false;
this.data[type][idx] = Object.assign({}, this.data[type][idx], patch);
this.save();
return true;
}


deleteItem(type, id) {
this.data[type] = this.data[type].filter(i => i.id !== id);
this.save();
}


clearAll() {
this.data = { tasks: [], notes: [], schedule: [] };
this.save();
}
}