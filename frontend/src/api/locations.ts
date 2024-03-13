import { api } from './api';

export const uploadLocationCsv = async (file: File) => {
  const form = new FormData();
  form.append('file', file);
  const response = await api.post('/location/csv', form);
  return response.status >= 200 && response.status < 400;
};
