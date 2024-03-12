import simpleRestProvider from 'ra-data-simple-rest';

export const restProvider = simpleRestProvider(import.meta.env.VITE_API_BASE);
