import jsonServerProvider from 'ra-data-json-server';

export const jsonProvider = jsonServerProvider(import.meta.env.VITE_API_BASE);
