import { api } from './api';

export const uploadCategotyCsv = async (file: File) => {
  const form = new FormData();
  form.append('file', file);
  const response = await api.post('/category/csv', form);
  return response.status >= 200 && response.status < 400;
};
