export function formatDateISO(dateStr) {
if (!dateStr) return '-';
const d = new Date(dateStr);
if (Number.isNaN(d.getTime())) return '-';
return d.toLocaleDateString('id-ID', { year: 'numeric', month: 'long', day: 'numeric' });
}


export function isValidDate(dateStr) {
if (!dateStr) return false;
const d = new Date(dateStr);
return !Number.isNaN(d.getTime());
}