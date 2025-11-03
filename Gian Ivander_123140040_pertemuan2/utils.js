// Minimal util functions — menggunakan arrow functions
export const $ = (sel) => document.querySelector(sel);
export const createEl = (tag, attrs = {}) => Object.assign(document.createElement(tag), attrs);
export const timePad = (n) => (n < 10 ? '0' + n : '' + n);
export const formatDateTime = (iso) => {
if (!iso) return '';
const d = new Date(iso);
return d.toLocaleString();
};